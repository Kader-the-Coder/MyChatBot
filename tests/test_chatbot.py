"""Check the outputs of all functions in the chatbot module"""

#------------------------------Imports---------------------------------
#pylint: disable=import-error
#pylint: disable=wrong-import-position
import os
import sys
ROOT = os.path.dirname(__file__).replace("\\tests","\\")
sys.path.append("".join([ROOT, "chatbots"]))
sys.path.append("".join([ROOT, "chatbots\\components"]))
from chatbot import chatbot

#------------------------------Unit test-------------------------------

sentence = input("Test: ")
tempA = chatbot(sentence, "locked_room", 0)
print(tempA)
