from loaders_and_savers import _load_json
from helper_functions import DiagramSaver
from enums import DiagramName,BoxProperties
from objet_color_dict import hex_dict
from highlighted_entry_generator import AnnotationViewer

import sys
import json
import random
from enum import Enum
from PyQt5.QtWidgets import (
    QApplication
)

#config_name = 'coco/rebuttal_evals/cherry_picking_selected' #into sws
    # diagram_title = DiagramName.REBUTTAL.value
    # subtitle = 'rebuttal_3'
    # prompt_number = 1
    # sample_numbers = [0]

highlighted_entries = {
    1: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [-20,-20]
    },
    5: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [10,20]
    },
    6: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [-40,-10]
    },
    8: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [10,140]
    },
    9: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [10,190]
    },
    10: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [-20,80]
    },
    17: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [-55,20]
    },
    18: {
        BoxProperties.EDGE_COLOR: hex_dict['car'],
        BoxProperties.TEXT_OFFSET: [150,0]
    },
    22: {
        BoxProperties.EDGE_COLOR: hex_dict['frisbee'],
        BoxProperties.TEXT_OFFSET: [20,20]
    },
    25: {
        BoxProperties.EDGE_COLOR: hex_dict['car'],
        BoxProperties.TEXT_OFFSET: [25,-20]
    },
    28: {
        BoxProperties.EDGE_COLOR: hex_dict['person'],
        BoxProperties.TEXT_OFFSET: [10,90]
    }
}

if __name__ == '__main__':
    #current_scene_instance = "/12/27" #  [0, 14, 27]

    # FOR the generation of highlighted entries
    app = QApplication(sys.argv)
    json_file = "/BS/inter_img_rep/work/diagram_maker/layouts_json/test_layout.json"
    viewer = AnnotationViewer(json_file)
    
    viewer.show()
    app.exec_()

    # AFTER the generation of highlighted entries
    highlighted_entries = _load_json("/BS/inter_img_rep/work/diagram_maker/highlighted_entries/test_highlighted_entries.json")

    # after the generation of highlighted entries
    diagram_saver = DiagramSaver()
    print(DiagramName.MAIN_RESULTS.value)
    diagram_saver(
        highlighted_entries["highlighted_entries"],
        diagram_type = DiagramName.MAIN_RESULTS.value,
        layout_path=json_file,
        pdf_path = "/BS/inter_img_rep/work/diagram_maker/final_layouts/test_layout.pdf")
    print('Program Complete')
