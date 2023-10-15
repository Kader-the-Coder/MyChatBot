"""This module deals with determining properties of a sentence"""

#------------------------------Imports---------------------------------

from reader import read_patterns    #pylint: disable=import-error

#------------------------------Function--------------------------------

def loader(sentence, nlp:object, matcher:object) -> (list|None):
    """Returns a list if the supplied sentence is of a particular type
    The returned list will have 2 indexes.
    * index 0 = the sentence type ("question", "statement" or "request")
    * index 1 = span of text that determined the sentence type.
    """
    sentence = nlp(sentence)
    matcher.add("request", read_patterns("request"))
    matcher.add("question", read_patterns("question"))
    matches = matcher(sentence)
    if matches:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = sentence[start:end]  # The matched span
            return [string_id, span, sentence]
    return None
