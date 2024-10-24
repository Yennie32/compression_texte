text = "qu'elle est... » ). expert en utilisabilite des"

dictionary_ref = {'texte': '1',
 'lorem': '2',
 'qui': '3',
 'donc': '4',
 'est': '5',
 'que': '6',
 'pour': '7',
 'ceci': '8',
 'faux-texte': '9',
 'dans': '10',
 'plus': '11',
 'avec': '12'}

words = ['mais', 'ceci', 'est', 'un', 'long', 'faux-texte']

# split the text into a list
def splitting_text (text) :
    split_text = text.split()
    return split_text

# print(splitting_text(text))

splitted = splitting_text(text)

# join the list back to a text
def joining_text(text):
    join_text = " ".join(text)
    return join_text

# print(joining_text(splitted))

# associate key/value. return words which are not in dictionary
def assoc_dictionary(dico, words):
    finded = []
    for word in words :
        if word in dico :
            x = dico.get(word)
            finded.append(x)
            print("finded1", finded)
        else :
            finded.append(word)
            print("finded2", finded)
    return finded

print("result", assoc_dictionary(dictionary_ref, words))