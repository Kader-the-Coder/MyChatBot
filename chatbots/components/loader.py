"""XXX"""
#pylint: disable=import-error
import spacy
from spacy.matcher import Matcher
from reader import read_patterns

nlp = spacy.load("en_core_web_lg")


def load_type(sentence):
    """XXX""" 
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


def load_target(sentence):
    """XXX""" 
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


def load_action(sentence):
    """XXX""" 
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

