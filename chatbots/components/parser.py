import spacy
warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)
nlp = spacy.load("en_core_web_lg")

def parse_input(sentence):
    """XXX""" 
    sentence = nlp(sentence)
    input_type = determine_type(sentence) or ["type", ""]
    input_target = determine_target(sentence) or ["target", ""]
    input_action = determine_action(sentence) or ["action", ""]
    return {
        input_type[0]: sentence,
        input_target[0]: nlp(input_target[1]),
        input_action[0]: nlp(input_action[1])
        }



#------------------------------UNIT TEST-------------------------------

if __name__  == "__main__":
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
