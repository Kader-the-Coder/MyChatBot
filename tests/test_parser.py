"""Check the outputs of all functions in the parse_input module"""

#------------------------------Imports---------------------------------

import os
import sys
ROOT = os.path.dirname(__file__).replace("\\tests","\\")
sys.path.append("".join([ROOT, r"chatbots\components"]))
from parse_input import parse_input
import spacy
nlp = spacy.load("en_core_web_lg")

#------------------------------Unit test-------------------------------



while True:
    request = input("TEST: ")
    print("dep_: ", " ".join(x.dep_ for x in nlp(request)), end="")
    print()
    print("lemma_: ", " ".join(x.lemma_ for x in nlp(request)), end="")
    print()
    print("pos_: ", " ".join(x.pos_ for x in nlp(request)), end="")
    print("\n")
    print("RETURN:",parse_input(request))
    print("------------------------")
