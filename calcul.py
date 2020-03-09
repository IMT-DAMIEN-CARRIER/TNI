# Programme servant à compter le nombre d'occurences
# d'une lettre dans un texte
msg = "ceci est un message test"

def calcul(msg) :
    # tab = [[lettre, occcurence], [lettre, occurence], ...]
    tab = []
    for i in range(0, len(msg)):
        existInTab = False
        for j in range(0, len(tab)):
            if msg[i] == tab[j][0]:
                tab[j][1] += 1
                existInTab = True
        if not existInTab:
            tab.append([msg[i], 1])
    print(tab)
    print("Longueur totale de la string : ", len(msg));
# calcul(msg)

def openFile():
    f = open(".\\test.TXT")
    print(f)
    texte = f.read()
    print(texte)
    f.close()
openFile()