"""This module is used to test all functions in the loader module"""
#pylint: disable=import-error
#pylint: disable=wrong-import-position

#------------------------------Imports---------------------------------

import os
import sys
ROOT = os.path.dirname(__file__).replace("\\tests","\\")
sys.path.append("".join([ROOT, r"chatbots\components"]))
from reader import read_scenes, read_patterns

#------------------------------Unit test-------------------------------

sentence = input("Test: ")
tempA = read_scenes(sentence)
tempB = read_patterns(sentence)

print(tempA, tempB, sep="\n")
