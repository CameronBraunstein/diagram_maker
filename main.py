from helper_functions import DiagramSaver
from enums import DiagramName,BoxProperties
from objet_color_dict import hex_dict

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
    diagram_saver = DiagramSaver()
    diagram_saver(
        highlighted_entries=highlighted_entries,
        diagram_type = DiagramName.MAIN_RESULTS.value,
        layout_path='layouts_json/initial_layout.json',
        pdf_path = 'final_layouts/layout.pdf')
    print('Program Complete')
