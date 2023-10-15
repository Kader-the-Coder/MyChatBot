import os
import spacy
DIR = os.path.dirname(__file__)

ACCURACY = 0.7
SPEECH_LIST = ["advmod", "nsubj"]



print("You are trapped in a brightly lit room. You need to get out.")
while True:
    user_input = input("ME: ")
    print("??:",chatbot(user_input))
