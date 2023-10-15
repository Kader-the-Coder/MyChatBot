import spacy

def chatbot(sentence:str):
    """XXX""" 
    sentence = parse_input(sentence)
    # Break up data so that 'values' can be compared.
    if "question" in sentence:
        data = load_scene(SCENE, "question")
        temp = 'question'
    elif "request" in sentence:
        return "I don't do requests. I only answer questions."

    key_list = list(data.keys())    # Responses
    val_list = list(data.values())  # Keywords matching a response.
    # Determine best response.
    for i,sub_list in enumerate(val_list):
        for j,token in enumerate(sub_list):
            val_list[i][j] = token.similarity(sentence[temp])

    response = [mean(x) for x in val_list]  # list of response similarities
    # Check if best response is a valid response
    if max(response) >= ACCURACY:
        response = key_list[response.index(max(response))]  # Best response as text
        return "".join(response.text)
    return "That makes no sense"