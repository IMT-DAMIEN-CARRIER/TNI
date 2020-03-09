#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programme servant à compter le nombre d'occurences
# d'une lettre dans un texte
from operator import itemgetter

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
    return tab

def writeProba(strlength, tab):
    for i in range(0, len(tab)):
        tab[i].append(tab[i][1]/strlength)
    return tab

def printtab(tab):
    for elt in tab:
        print(elt);

def openFile():
    f = open(".\\zola.txt", encoding="utf-8")
    print(f)
    texte = f.read()
    tab = writeProba(len(texte), calcul(texte))
    tab = sorted(tab, key=lambda x: -x[1])
    printtab(tab)
    f.close()
openFile()