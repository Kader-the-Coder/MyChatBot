"""This module deals with determining properties of a sentence"""

import spacy
from spacy.matcher import Matcher
from reader import read_patterns

nlp = spacy.load("en_core_web_lg")


def load_type(sentence) -> (list|None):
    """Returns a list if the supplied sentence is of a particular type
    The returned list will have 2 indexes.
    * index 0 = the sentence type ("question", "statement" or "request")
    * index 1 = span of text that determined the sentence type.
    """
    sentence = nlp(sentence)
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add("request", read_patterns("request"))
    matcher.add("question", read_patterns("question"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span.text]
    return None


def load_target(sentence) -> list:
    """Returns a list if the supplied sentence has a target
    The returned list will have 2 indexes.
    * index 0 = "target"
    * index 1 = the span of text that determined that the supplied
      sentence had a target
    """
    sentence = nlp(sentence)
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add("target", read_patterns("target"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span.text]
    return None


def load_action(sentence) -> list:
    """Returns a list if the supplied sentence qualifies as a question
    The returned list will have 2 indexes.
    * index 0 = "action"
    * index 1 = the span of text that determined that the supplied
      sentence implied an action.
    """ 
    sentence = nlp(sentence)
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add("action", read_patterns("action"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span.text]
    return None
