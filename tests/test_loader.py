"""Check the outputs of all functions in the loader module"""

#------------------------------Imports---------------------------------
#pylint: disable=import-error
#pylint: disable=wrong-import-position
import os
import sys
ROOT = os.path.dirname(__file__).replace("\\tests","\\")
sys.path.append("".join([ROOT, "chatbots\\components"]))
from loader import loader

#------------------------------Unit test-------------------------------
import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_lg")
matcher = Matcher(nlp.vocab, validate=True)

while True:
    sentence = input("Test: ")
    print("dep_: ", " ".join(x.dep_ for x in nlp(sentence)), end="")
    print()
    print("lemma_: ", " ".join(x.lemma_ for x in nlp(sentence)), end="")
    print()
    print("pos_: ", " ".join(x.pos_ for x in nlp(sentence)), end="")
    print("\n")
    print("RETURN:", loader(sentence, nlp, matcher))
    print("------------------------")
