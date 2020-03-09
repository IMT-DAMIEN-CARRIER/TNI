# Programme servant à compter le nombre d'occurences
# d'une lettre dans un texte
# test louise

def calcul(msg) :
    # tab = [[lettre, occcurence], [lettre, occurence], ...]
    tab = []
    for i in range(0, msg.length):
        existInTab = False
        for elt in tab:
            if msg[i] == elt:
                msg[i, 1] += 1
        if not existInTab:
            msg.push([msg[i], 1])
