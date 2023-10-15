"""Check the outputs of all functions in the loader module"""
#pylint: disable=wrong-import-position

#------------------------------Imports---------------------------------

import os
import sys
ROOT = os.path.dirname(__file__).replace("\\tests","\\")
sys.path.append("".join([ROOT, r"chatbots\components"]))
from loader import load_type, load_target, load_action
import spacy
nlp = spacy.load("en_core_web_lg")

#------------------------------Unit test-------------------------------

sentence = input("Test: ")
sentence_type = load_type(sentence)
sentence_target = load_target(sentence)
sentence_action = load_action(sentence)

print("  type: ", sentence_type)
print("target: ", sentence_target)
print("action: ", sentence_action)
