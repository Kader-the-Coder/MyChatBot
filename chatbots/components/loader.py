import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_lg")

def load_type(sentence):
    """XXX""" 
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add("request", import_patterns("pattern_request"))
    matcher.add("question", import_patterns("pattern_question"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span.text]
    return None


def load_target(sentence):
    """XXX""" 
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add("target", import_patterns("pattern_target"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span.text]
    return None


def load_action(sentence):
    """XXX""" 
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add("action", import_patterns("pattern_action"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span.text]
    return None

