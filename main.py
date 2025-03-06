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
    current_scene_instance = "/1/23"

    # for the generation of highlighted entries
    app = QApplication(sys.argv)
    json_file = "/home/hepe00001/Desktop/neuro_explicit/generative_diffusion/cherry_pick/survey_benchmark"+current_scene_instance+".json"
    viewer = AnnotationViewer(json_file, current_scene_instance)
    
    viewer.show()
    app.exec_()

    highlighted_entries = _load_json("/home/hepe00001/diagram_maker/highlighted_entries"+current_scene_instance+".json")

    # after the generation of highlighted entries
    diagram_saver = DiagramSaver()
    print(DiagramName.MAIN_RESULTS.value)
    diagram_saver(
        highlighted_entries["highlighted_entries"],
        diagram_type = DiagramName.MAIN_RESULTS.value,
        layout_path=json_file,
        pdf_path = "/home/hepe00001/diagram_maker/final_layouts"+current_scene_instance+".pdf")
    print('Program Complete')
