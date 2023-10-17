"""XXX"""

#------------------------------Imports---------------------------------

import os
import spacy
from spacy.matcher import Matcher
from chatbots.chatbot import chatbot

#------------------------Initialise variables--------------------------

DIR = os.path.dirname(__file__)
nlp = spacy.load("en_core_web_lg")
matcher = Matcher(nlp.vocab, validate=True)
ACCURACY = 0.5

#----------------------------Execute code------------------------------

print("You are trapped in a brightly lit room. You need to get out.")
while True:
    sentence = input("ME: ")
    print("??:",chatbot(sentence, nlp, matcher, "locked_room", ACCURACY))
