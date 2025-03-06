from enum import Enum

class DiagramName(Enum):
    MAIN_RESULTS = 'main_updated'
    DISENTANGLEMENT = 'disentanglement'
    EDITING = 'editing'
    TEASER = 'teaser'
    METHOD = 'method'
    DIFFUSION_ABLATION = 'diffusion_ablation'
    ZERO_TEMP_ABL = 'zero_temp_ablation'
    GPT_TEMP_ABL = 'gpt_temp_ablation'
    METRIC_BREAKER = 'metric_breaker'
    REBUTTAL = 'rebuttal'
    BONUS = 'bonus'

class BoxProperties(Enum):
    HIGHLIGHTED_ENTRIES = 'highlighted_entries'
    EDGE_COLOR = 'edge_color'
    TEXT_OFFSET  = 'text_offset'
    BOLDED_FRAME = 'bolded_frame'
    BOX_NAME = 'box_name'
    HIDE_TEXT = 'hide_text'





def get_font_size(input):
    if input == DiagramName.MAIN_RESULTS.value:
        return 28 
    elif input == DiagramName.TEASER.value:
        return 30
    elif input == DiagramName.METHOD.value:
        return 40
    elif input == DiagramName.DISENTANGLEMENT.value:
        return 25
    elif input == DiagramName.EDITING.value:
        return 25
    elif input == DiagramName.DIFFUSION_ABLATION.value:
        return 25
    elif input == DiagramName.BONUS.value:
        return 28
    elif input == DiagramName.REBUTTAL.value:
        return 28
    else:
        raise Exception(f'Font size not defined for {input}')
        return 20


def get_pad_size(input):
    if input == DiagramName.MAIN_RESULTS.value:
        return 0.14
    elif input == DiagramName.TEASER.value:
        return 0.14
    else:
        raise Exception(f'Pad size not defined for {input}')
        return 0.3