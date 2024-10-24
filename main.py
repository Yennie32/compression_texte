from collections import defaultdict

text1 = "qu'elle est... » ). expert en utilisabilite des"

dictionary_ref1 = {'texte': '1',
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

text2 = ['mais', 'ceci', 'est', 'un', 'long', 'faux-texte']
text3 = "généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement sur l'aspect graphique. ce texte a pour autre avantage d'utiliser des mots de longueur variable, essayant de simuler une occupation normale. la méthode simpliste consistant à copier-coller un court texte plusieurs fois ( « ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte » ) a l'inconvénient de ne pas permettre une juste appréciation typographique du résultat final. il circule des centaines de versions différentes du lorem ipsum, mais ce texte aurait originellement été tiré de l'ouvrage de cicéron, de finibus bonorum et malorum ( liber primus ), texte populaire à cette époque, dont l'une des premières phrases est : « neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... » ( « il n'existe personne qui aime la souffrance pour elle-même, ni qui la recherche ni qui la veuille pour ce qu'elle est... » ). expert en utilisabilité des sites web et des logiciels, jakob nielsen souligne que l'une des limites de l'utilisation du faux-texte dans la conception de sites web est que ce texte n'étant jamais lu, il ne permet pas de vérifier sa lisibilité effective. la lecture à l'écran étant plus difficile, cet aspect est pourtant essentiel. nielsen préconise donc l'utilisation de textes représentatifs plutôt que du lorem ipsum. on peut aussi faire remarquer que les formules conçues avec du faux-texte ont tendance à sous-estimer l'espace nécessaire à une titraille immédiatement intelligible, ce qui oblige les rédactions à formuler ensuite des titres simplificateurs, voire inexacts, pour ne pas dépasser l'espace imparti. contrairement à une idée répandue, le faux-texte ne donne même pas un aperçu réaliste du gris typographique, en particulier dans le cas des textes justifiés : en effet, les mots fictifs employés dans le faux-texte ne faisant évidemment pas partie des dictionnaires des logiciels de pao, les programmes de césure ne peuvent pas effectuer leur travail habituel sur de tels textes. par conséquent, l'interlettrage du faux-texte sera toujours quelque peu supérieur à ce qu'il aurait été avec un texte réel, qui présentera donc un aspect plus sombre et moins lisible que le faux-texte avec lequel le graphiste a effectué ses essais. un vrai texte pose aussi des problèmes de lisibilité spécifiques ( noms propres, numéros de téléphone, retours à la ligne fréquents, composition des citations en italiques, intertitres de plus de deux lignes ... ) qu'on n'observe jamais dans le faux-texte."

# split the text into a list
def splitting_text (text) :
    split_text = text.split()
    return split_text

# print("splitted text", splitting_text(text))

splitted = splitting_text(text1)

# join the list back to a text
def joining_text(text):
    join_text = " ".join(text)
    return join_text

# print("joined text", joining_text(splitted))

# associate key/value. return words which are not in dictionary
def assoc_dictionary(dico, words):
    finded = []
    for word in words :
        if word in dico :
            x = dico.get(word)
            finded.append(x)
            #print("finded1", finded)
        else :
            finded.append(word)
            #print("finded2", finded)
    return finded

#print("result", assoc_dictionary(dictionary_ref, text2))

# compress the orginal text
def lets_compress(text):
    splitting = splitting_text(text)
    #print("splitting", splitting)
    associating = assoc_dictionary(dictionary_ref, splitting)
    #print("associating", associating)
    joining = joining_text(associating)
    #print("joining", joining)
    return joining

#print("compress", lets_compress(text3))

# decompress the original text
inv_dictionary_ref = {v: k for k, v in dictionary_ref1.items()}
#print("inv_dictionary_ref", inv_dictionary_ref)

def lets_decompress(text):
    splitting = splitting_text(text)
    #print("splitting", splitting)
    associating = assoc_dictionary(inv_dictionary_ref, splitting)
    #print("associating", associating)
    joining = joining_text(associating)
    #print("joining", joining)
    return joining

#print("lets_decompress", lets_decompress(text3))
# creating a new dict where value are the number of occurences of words in the text
def create_dico(text):
    dictionary_ref2 = defaultdict(int) # creating values starting from 0
    split_text = text.split()
    print(split_text)
    for words in split_text:
        dictionary_ref2[words] += 1
    return dict(dictionary_ref2)

    # *** FOR LOOP METHOD ***
    # for word in split_text:
    #     if word in dictionary_ref2 :
    #         dictionary_ref2[word] += 1
    #     else :
    #         dictionary_ref2[word] = 1
    # return dictionary_ref2

print(create_dico(text3))