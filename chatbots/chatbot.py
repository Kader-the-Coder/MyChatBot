"""xxx"""
#------------------------------Imports---------------------------------
#pylint: disable=import-error
from numpy import mean
from chatbots.components.loader import loader

def chatbot(sentence:str, nlp:object, matcher:object, scene:str, accuracy:int):
    """XXX""" 
    sentence = loader(sentence, nlp, matcher)
    if sentence:
        if sentence[0] == "question":
            return "Hi. You asked a question."
        if sentence[0] == "request":
            return "Hey. You made a request."
    return "What you just said makes no sense."