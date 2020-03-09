#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programme servant à compter le nombre d'occurences
# d'une lettre dans un texte
from math import *

def calcul(msg):
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
    hFinale = 0

    for i in range(0, len(tab)):
        moy = tab[i][1] / strlength
        hFinale += (moy * log2(1/moy))
        tab[i].append(moy)

    print("L'entropie de notre alphabet est de : ", hFinale);

    return tab


def printtab(tab):
    for elt in tab:
        print(elt);


def openFile():
    f = open(".\\exemple1.txt", encoding="utf-8")
    print(f)
    texte = f.read()
    tab = writeProba(len(texte), calcul(texte))
    tab = sorted(tab, key=lambda x: -x[1])
    printtab(tab)
    f.close()

# openFile()

def openRawFile():
    f = open(".\\lena_gray.raw", encoding="utf-8")
    texte = f.read()
    tabTexte = texte.split(" ")
    print(tabTexte)
    tab = writeProba(len(tabTexte), calcul(tabTexte))
    tab = sorted(tab, key=lambda x: -x[1])
    printtab(tab)
    f.close()

openRawFile()