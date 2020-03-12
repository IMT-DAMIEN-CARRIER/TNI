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

# printtab(tabProbas)

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
    """
    :return: un tableau associatif de type [numero de l'état] = (cumul, pourcentage)
    """
    etats = dict()
    cumul = 0

    for i in range(0, len(tabProbas)):
        cumul += tabProbas[i][2]
        etats[tabProbas[i][0]] = [cumul, (tabProbas[i][2]*100)/len(tabProbas)]
    return etats

# print(fonctionCumulative())

def taggage():
    """
    pour chaque séquence à coder, choisir un tag dans l'intervalle corresondant au numéro de l'état
    ça deviendra le nouvel intervalle
    :return:
    """
    code = []
    tabSeq = tableauSequence()
    cumulative = fonctionCumulative()
    # intervalle
    low = 0
    up = 1

    for i in tabSeq:
        # numéro du premier état
        etat = i[0]

        # nouvel intervalle
        low = cumulative[etat][0]

        # Définition de la borne supérieure de l'intervalle
        k = 1
        while k < len(cumulative):
            if (int(etat) + k) in cumulative:
                up = cumulative[str(int(etat)+k)][0]
                break
            else:
                k += 1

        # on choisi notre premier tag
        tag = (up + low)/2

        code.append(tag)  # TODO: utiliser un tag binaire

    return code

tags = taggage()
print("taggage : {} \r\ntaille du tableau de codes : {}".format(tags, len(tags)))

# TODO : mettre les tags dans un fichier et regarder la taille du fichier (pour voir la compression)