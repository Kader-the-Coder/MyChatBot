"""This module deals with determining properties of a sentence"""

#------------------------------Imports---------------------------------

from loader import load_type, load_target, load_action

#------------------------------Unit test-------------------------------

def parse_input(sentence):
    """XXX""" 
    input_type = load_type(sentence) or ["type", ""]
    input_target = load_target(sentence) or ["target", ""]
    input_action = load_action(sentence) or ["action", ""]
    return {
        input_type[0]: sentence,
        input_target[0]: input_target[1],
        input_action[0]: input_action[1]
        }