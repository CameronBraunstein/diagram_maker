import os
import sys
import json
import random
from enum import Enum
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QPushButton, QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QVBoxLayout, QWidget, QLabel, QGraphicsTextItem, QHBoxLayout
)
from PyQt5.QtGui import QColor, QPen, QBrush, QPainter, QFont
from PyQt5.QtCore import Qt, QRectF

hex_dict = {
    'highway': '#e79af0',
    'street': '#f0a8e7',
    'frisbee': '#ed094f',
    'dining table': '#332a89',
    'knife': '#3063f0',
    'sandwich': '#f0a8e7',
    'fork': '#e7a8f0',
    'cup': '#ba175a',
    'truck': '#ba175a',
    'mirror': '#e79af0',
    'sconce': '#ba175a',
    'coffee maker':'#85431c',
    'faucet': '#52a0cb',
    'hood': '#c16e21',
    'work surface': '#e6e61d',
    'kitchen island': '#5a21d6',
    'house': '#3f5dd5',
    'sky': '#3063f0',
    'tree': '#69130b',
    'road': '#55065e',
    'building': '#3063f0',
    'signboard': '#13690b',
    'car': '#13690b',
    'fence': '#e7a30c',
    'hill':  '#049c2c',
    'mountain': '#babf01',
    'bathtub':  '#07c8cc',
    'wall':  '#d1b804',
    'floor':  '#2106b9',
    'sink':  '#e514d3',
    'windowpane': '#98e0d7',
    'light': '#8a5a11',
    'curtain': '#6d0dc1',
    'ceiling': '#e6e61d',
    'countertop':  '#7f0d0d',
    'plant': '#0d7f0d', 
    'toilet':  '#3bdb50',
    'embankment': '#543c42',
    'door': '#c02706',
    'building':  '#31b586',
    'grass':  '#ec1de0',
    'flower':  '#ef50e6',
    'palm':  '#693d06',
    'pot':  '#2f1f2e',
    'roof':  '#760ee2',
    'bucket':  '#557162',
    'chair': '#892a58',
    'cabinet': '#2a892a',
    'table': '#332a89',
    'cushion': '#6794ab',
    'armchair': '#df1077',
    'sofa': '#94db12',
    'painting': '#ff0087',
    'coffee table': '#23efe5',
    'decoration': '#d80c0c',
    'blind': '#8f21ce',
    'lamp': '#1cc1b1',
    'ottoman': '#e3f428',
    'rug': '#ef7408',
    'chandelier': '#08ef81',
    'counter': '#5e6327',
    'sidewalk': '#356b64',
    'box': '#5e103c',
    'post': '#14aa95',
    'person': '#bbd01c',
    'manhole': '#3616b7',
    'bench':  '#701f3c',
    'flower bed': '#9113a1',
    'path': '#3f1145',
    'flower pot': '#d15707',
    'garden': '#66cd8e',
    'umbrella': '#c94fc5',
    'mast':  '#a0889f',
    'panda':  '#ec2709',
    'bowl':  '#e6e61d',
    'buffet':  '#e6e61d',
    'pillow': '#1dae49',
    'bed': '#653b9b',
    'book': '#577bd3',
    'skyscraper': '#97a4c4',
    'river': '#2348a3',
    'television': '#7e828c',
    'bookshelf': '#84665b',
    'window': '#98e0d7',
    'floor lamp': '#9e65d6',
    'lamp post':  '#433b5c',
    'bicycle': '#3abcc3',
    'streelight': '#f8ed0b',
    'fireplace': '#f48d05',
    'candlestick': '#dfdbb8',
    'fan': '#24cedd',
    'step': '#a13d32',
    'railing': '#b845b9',
    'stairs': '#a13d32',
    'postbox': '#98349b',
    'streetlight': '#f30d0d',
    'minibike':  '#1876d7',
    'traffic light': '#27d718',
    'vending machine': '#daa4e0',
    'trade name': '#c6892d',
    'ashcan': '#b9afa1',
    'seal':  '#625747',
    'elephant': '#aca292',
    'shirt' : '#1876d7',
    'goal': '#45d2ae',
    'puf': '#e2489a',
    'animal':  '#d48323',
    'numeral': '#85a353',
    'controls': '#537ca3',
    'tomb':'#9aa8b5',
    'premade house': '#886fb2',
    'spring': '#3eb0c3',
    'power point': '#e2c436',
    'flood': '#5daed5',
    'olives': '#2c6f13',
    'cd':  '#e3ede0',
    'station': '#60202e',
    'shelter': '#6152b6',
    'bag': '#bb5f73',
    'glass': '#aaece8',
    'refrigerator':'#0f8c85',
    'towel':  '#2ecc15',
    'bottle': '#7381b8',
    'bike': '#3abcc3',

}

class BoxProperties(Enum):
    HIGHLIGHTED_ENTRIES = 'highlighted_entries'
    EDGE_COLOR = 'edge_color'
    TEXT_OFFSET = 'text_offset'
    BOLDED_FRAME = 'bolded_frame'
    HIDE_TEXT = 'hide_text'
    BOX_NAME = 'box_name'

class BoundingBoxItem(QGraphicsRectItem):
    def __init__(self, x, y, w, h, color, index, caption, label_item, parent=None):
        super().__init__(parent)  # ✅ Fixing constructor

        self.setRect(QRectF(x, y, w, h))  # ✅ Correct interpretation
        self.setPen(QPen(Qt.black, 2))
        self.default_color = QColor(color)
        self.default_color.setAlpha(100) 
        self.setBrush(QBrush(Qt.NoBrush))
        self.index = index
        self.caption = caption
        self.highlighted = False
        self.label_item = label_item
        self.label_item.setVisible(False)


    def toggle_highlight(self, hex_dict, highlighted_entries):
        if self.highlighted:
            self.setBrush(QBrush(Qt.NoBrush))
            self.label_item.setVisible(False)  # Hide label when unhighlighted
            highlighted_entries.pop(self.index, None)  # Remove from JSON
        else:
            highlight_color = QColor(hex_dict[self.caption])
            highlight_color.setAlpha(100)  # Set transparency
            self.setBrush(QBrush(self.default_color))  # ✅ No error now
            self.label_item.setVisible(True)  # Show label when highlighted
            highlighted_entries[self.index] = {
                BoxProperties.EDGE_COLOR.value: hex_dict[self.caption],
                BoxProperties.TEXT_OFFSET.value: [int(self.x()), int(self.y())],
                BoxProperties.BOX_NAME.value: self.caption
            }
        self.highlighted = not self.highlighted



class LabelBoxItem(QGraphicsRectItem):
    def __init__(self, text, x, y, parent=None): # (anno['caption'], x, y - 30, bbox_item)
        super().__init__(parent)
        self.text_item = QGraphicsTextItem(text, self)
        self.text_item.setDefaultTextColor(Qt.black)
        scale_factor = 2  # Increase this to make the boxes appear larger but want to keep the font the same size
        font = QFont("Arial", int(28 / scale_factor))  
        self.text_item.setFont(font)
        text_rect = self.text_item.boundingRect()

        margin = 0
        self.setRect(0, 0, text_rect.width() + 2 * margin, text_rect.height() + 2 * margin)
        self.setBrush(QBrush(Qt.white))
        self.setPen(QPen(Qt.black, 2))

        self.setPos(x, y)  # Initial position

        # Allow movement
        self.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        self.setFlag(QGraphicsRectItem.ItemSendsScenePositionChanges, True)  # Enable event detection


        # bounding boxes of the box surronuding the object
        self.bb_x = x
        self.bb_y = y

    def mouseReleaseEvent(self, event):
        """Update the offset when the label is moved."""
        offset = self.get_offset()
        super().mouseReleaseEvent(event)

    def get_offset(self):
        """Calculate the offset relative to the bounding box after movement."""
        text_box_x, text_box_y = self.x(), self.y()  # Get updated position of the text box
        
        self.offset_x = int(text_box_x - self.bb_x)
        self.offset_y = int(text_box_y - self.bb_y)
        print(f"Text box position: {text_box_x}, {text_box_y}, {self.bb_x}, {self.bb_y}, offset: {self.offset_x}, {self.offset_y}")
        return [int(self.offset_x), int(self.offset_y)]

class AnnotationViewer(QMainWindow):
    def __init__(self, json_file, current_scene_instance):
        super().__init__()
        self.setWindowTitle("Annotation Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.json_data = self.load_json(json_file)
        self.highlighted_entries = {}
        self.hex_dict = {}
        self.bbox_items = []  # Store bounding box references
        self.initUI()
        self.current_scene_instance = current_scene_instance
        self.offset_x = 0
        self.offset_y = 0

    def load_json(self, json_file):
        with open(json_file, 'r') as f:
            return json.load(f)

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout(central_widget)

        # Title Label
        title_label = QLabel(f"{self.json_data['full_prompt']}")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.setContentsMargins(0, 0, 0, 0)
        

        main_layout.addWidget(title_label)

        # Horizontal layout for graphics view and button panel
        content_layout = QHBoxLayout()

        # Graphics Scene and View
        self.scene = QGraphicsScene(0, 0, 511, 511)
        self.view = QGraphicsView(self.scene)
        self.view.setMinimumSize(1200, 800)
        
        self.view.setRenderHint(QPainter.Antialiasing)

        self.scene.setSceneRect(0, 0, 511, 511)
        self.view.setSceneRect(0, 0, 511, 511)

        # ✅ Apply scaling factor
        scale_factor = 2  # Increase this to make the boxes appear larger
        self.view.setTransform(self.view.transform().scale(scale_factor, scale_factor))


        content_layout.addWidget(self.view, 2)

        # Button Panel
        self.button_widget = QWidget()
        self.button_layout = QVBoxLayout(self.button_widget)
        self.button_widget.setFixedWidth(200)
        content_layout.addWidget(self.button_widget, 1)

        main_layout.addLayout(content_layout)
        
        self.load_annotations()

        # Save Button
        save_button = QPushButton("Save Highlights")
        save_button.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        save_button.clicked.connect(self.save_highlighted_entries)
        self.button_layout.addWidget(save_button)

    def load_annotations(self):
        for idx, anno in enumerate(self.json_data['annos']):
            x, y, w, h = anno['bbox']

            # Clip x and y to ensure they are within [0, 511]
            x = max(0, min(x, 511))
            y = max(0, min(y, 511))

            # Ensure width and height do not extend beyond 511
            w = min(w, 511 - x)  # Ensure x + w <= 511
            h = min(h, 511 - y)  # Ensure y + h <= 511


            #color = QColor(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255), 100)
            #hex_color = '#{:02x}{:02x}{:02x}'.format(color.red(), color.green(), color.blue())
            self.hex_dict[anno['caption']] = hex_dict.get(anno['caption'], "#000000")  # Default to black if not found


            # Create Label Box
            label_item = LabelBoxItem(anno['caption'], x, y)

            # Create Bounding Box and link it to the label
            bbox_item = BoundingBoxItem(x, y, w, h, self.hex_dict[anno['caption']], idx, anno['caption'], label_item)
            self.scene.addItem(bbox_item)
            self.bbox_items.append(bbox_item)  # Store for easy access
            self.scene.addItem(label_item)

            # Initially hide the label
            label_item.setVisible(False)

            # Create Button for Highlighting
            btn = QPushButton(anno['caption'])
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, item=bbox_item: self.on_button_clicked(checked, item))
            self.button_layout.addWidget(btn)


    def on_button_clicked(self, checked, item):
        """Ensure button click event is triggering toggle_highlight"""
        #print(f"Button clicked for {item.caption}, checked: {checked}")  # Debugging
        item.toggle_highlight(self.hex_dict, self.highlighted_entries)

    def save_highlighted_entries(self):
        save_path = "/home/hepe00001/diagram_maker/highlighted_entries"+self.current_scene_instance+".json"
        print(save_path)
        highlighted_entries = {}

        # Iterate over bounding boxes (we stored them in self.bbox_items)
        for index, bbox_item in enumerate(self.bbox_items):
            
            if bbox_item.highlighted:  # Check if highlighted
                bbox_index = bbox_item.index
                caption = bbox_item.caption

                # Find corresponding LabelBoxItem
                label_offset = [0, 0]  # Default offset
                for label in self.scene.items():
                    if isinstance(label, LabelBoxItem) and label.text_item.toPlainText() == caption:
                        
                        label_offset = label.get_offset()
                        x_offset, y_offset = label.offset_x, self.offset_y
                        print(f"Found label {caption} at offset {label_offset}")
                        label_offset = [x_offset, y_offset]
                        print(f"Found label {caption} at offset {label_offset}")

                        break  # Found the label, stop searching

                # Store in dictionary
                highlighted_entries[int(index)] = {
                    BoxProperties.EDGE_COLOR.value: self.hex_dict[caption],  
                    BoxProperties.TEXT_OFFSET.value: label_offset,
                    BoxProperties.BOX_NAME.value: caption
                }


        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save to JSON
        with open(save_path, 'w') as f:
            json.dump({BoxProperties.HIGHLIGHTED_ENTRIES.value: highlighted_entries}, f, indent=4)

        print(f"Saved highlighted entries to {save_path}")