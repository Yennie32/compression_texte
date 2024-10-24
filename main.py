text = "qu'elle est... » ). expert en utilisabilite des"

def splitting_text (text) :
    split_text = text.split()
    return split_text

splitted = splitting_text(text)

def joining_text(text):
    join_text = " ".join(text)
    return join_text


print(splitting_text(text))
print(joining_text(splitted))
