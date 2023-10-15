"""XXX"""

import os
import json
DIR = os.path.dirname(__file__)
PATTERNS = os.path.join(DIR, "patterns.json")
SCENE = os.path.join(DIR, "locked_room.json")

def read_scenes(scene:__file__, input_type:str) -> dict:
    """Returns a dictionary from .json file.
    All keys and values in dictionary are nlp objects.
    """
    with open(scene, "r", encoding="utf-8-sig") as file:
        data = json.load(file)
    return {x:list(data[input_type][x]) for x in data[input_type]}


def read_patterns(pattern_type):
    """XXX""" 
    with open(PATTERNS, "r", encoding="utf-8") as file:
        data = json.load(file)
    return list(data[pattern_type])
