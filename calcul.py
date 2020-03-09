# Programme servant à compter le nombre d'occurences
# d'une lettre dans un texte

def calcul(msg) :
    # tab = [[lettre, occcurence], [lettre, occurence], ...]
    tab = []
    for i in range(0, msg.length):
        existInTab = false
        for elt in tab:
            if msg[i] == elt:
                msg[i, 1] += 1
        if !existInTab:
            msg.push([msg[i], 1])
