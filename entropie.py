from calcul import *
from scipy import *
from numpy import *

def openFile():
    f = open(".\\lena_gray.raw")
    print(f)
    texte = f.read()
    print(texte)
    f.close()
    return texte
# openFile()

tabPixel = openRawFile()
tabProbas = openProbasFile()

printtab(tabProbas)  # TODO : renvoyer le tableau des probas trié par ordre croissant des numéros d'états

def tableauSequence():
    """
    Crée un tableau des séquences de 8 elements
    :return:
    """
    tabSeq = []
    print("Début codeur")
    for c in range(0, len(tabPixel), 8):
        sequence = []
        for i in range(0, 8):
            # print("     c + i : " + str(c+i) + " alors que tabPixel fait " + str(len(tabPixel)))
            if (c+i) < len(tabPixel):
                sequence.append(tabPixel[c+i])
        tabSeq.append(sequence)
    return tabSeq
# tableauSequence()

def fonctionCumulative():
    pass