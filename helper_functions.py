import os
from loaders_and_savers import _load_json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
from PIL import Image

from objet_color_dict import hex_dict, hex_to_rgba
from enums import DiagramName, BoxProperties, get_font_size, get_pad_size



class DiagramSaver:
    def __init__(self):
        self.default_box_color = '#D3D3D3' 
        self.default_alpha = 0.2

    def __call__(self,highlighted_entries,diagram_type,layout_path, pdf_path ):
        # Ensure the directory exists
        
        bounding_boxes = _load_json(layout_path)
        frame_height, frame_width = 512, 512

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, frame_width)
        ax.set_ylim(frame_height, 0)
        ax.set_xticks([])
        ax.set_yticks([])

        for i, obj in enumerate(bounding_boxes['annos']):
            
            if 'opacity' in obj:
                if obj['opacity'] < 0.5:
                    print(f'Opacity less than 0.5, skipping {i}')
                    continue

            #x_min, y_min, box_width, box_height = obj['bbox']
            x_min = obj['bbox'][0]
            y_min = obj['bbox'][1]
            box_width = obj['bbox'][2]
            box_height = obj['bbox'][3]

            label = obj['caption']
            if len(obj['bbox'])==5:
                z = obj['bbox'][4]
                label = f'{label} ({z:.2f})'
            
            z_order = 1
            edgecolor = self.default_box_color
            facecolor = 'none'
            linewidth = 2
            alpha = self.default_alpha
            textbox_width = 2
            fontweight = 'normal'

            fontsize = get_font_size(diagram_type)
            print('fontsize:', fontsize)
            boxstyle_padding = get_pad_size(diagram_type)
            if str(i) in highlighted_entries.keys():
                entry_dict = highlighted_entries[str(i)]
                print(entry_dict.keys())
                if BoxProperties.BOX_NAME.value in entry_dict:
                    
                    edgecolor = hex_dict.get(entry_dict.get(BoxProperties.BOX_NAME.value), "#000000")  
                elif BoxProperties.EDGE_COLOR in entry_dict:
                    edgecolor = entry_dict[BoxProperties.EDGE_COLOR.value]
                if BoxProperties.BOLDED_FRAME in entry_dict:
                    linewidth = 4
                    alpha=0.4
                    textbox_width= 4
                    fontweight = 'heavy'
                z_order = 2

                facecolor = hex_to_rgba(edgecolor, alpha)
                if BoxProperties.TEXT_OFFSET.value in entry_dict:
                    x_offset, y_offset = entry_dict[BoxProperties.TEXT_OFFSET.value]
                else:
                    x_offset, y_offset = 0,0

                if (BoxProperties.HIDE_TEXT not in entry_dict) or (not entry_dict[BoxProperties.HIDE_TEXT]):
                    if label == 'panda bear':
                        label = 'panda'
                    if label == 'plant':
                        print('here with plant: x_min, y_min, box_width, box_height', x_min, y_min, box_width, box_height)
                    ax.text(x_min+x_offset, y_min+y_offset, label, verticalalignment='top', color='black',
                         bbox=dict(facecolor='white', 
                                   edgecolor='black', 
                                   boxstyle=f'round,pad={boxstyle_padding}', #was 0.3
                                   linewidth=textbox_width), 
                                   fontsize=fontsize,
                                   fontweight=fontweight)  # Added stretch parameter

            rect = patches.Rectangle((max(linewidth,x_min), max(linewidth,y_min)),min(box_width, frame_width-1-x_min), min(box_height, frame_height-1-y_min),
                linewidth=linewidth,  
                edgecolor=edgecolor,
                facecolor=facecolor,
                zorder=z_order)
            ax.add_patch(rect)

        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        plt.savefig(pdf_path,bbox_inches='tight', pad_inches =0.0,format='pdf')








