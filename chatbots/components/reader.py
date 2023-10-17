"""XXX"""

#------------------------------Imports---------------------------------

import os
import json
DIR = os.path.dirname(__file__)

#------------------------------Functions-------------------------------


def read_scenes(scene:str, input_type:str) -> dict:
    """Returns a dictionary from .json file.
    All keys and values in dictionary are nlp objects.
    """
    scene = os.path.join(DIR, f"data\\{scene}.json")
    with open(scene, "r", encoding="utf-8-sig") as file:
        data = json.load(file)
    return {x:list(data[input_type][x]) for x in data[input_type]}


def read_patterns(pattern_type:str) -> list:
    """Returns a list of patterns for a given type.
    * pattern_type: "question", "request", "target", "action"
    """
    pattern = os.path.join(DIR, "data\\patterns.json")
    with open(pattern, "r", encoding="utf-8") as file:
        data = json.load(file)
    return list(data[pattern_type])
