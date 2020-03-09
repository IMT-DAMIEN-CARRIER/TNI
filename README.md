# Traitement Numérique de l'Information

## Projet 1

###### Louise Robert - Alex Broussard - Damien Carrier

### I. Entropie d'un texte

#### 0. Introduction

Pour cette partie nous avons décidé de parcourir le texte pour regarder chaque caractère. Nous initialisons un tableau de la manière suivant : 

- Si le nouveau caractère n'existe pas dans le tableau on le rajoute et on initialise le nombre de fois ou il est présent à 1.

- Si il est déjà présent on incrémente de 1 sa présence

De cette manière nous pouvons avoir un tableau dynamique pour lire n'importe quel texte qui nous génère un alphabet aléatoire et personnalisé en fonction du texte entrée. 

Ensuite grace au compteur et la présence d'un caractère dans le texte on pourra calculer la probabilité, arrondi à 10<sup>-6</sup>, d'avoir ce caractère ainsi que l'entropie de l'alphabet générée.

#### 1. Code

```python

```

#### 2. Probabilité d'occurence de chaque lettre de l'alphabée

Voici ce que retourne le tableau *(nous avons choisi de ne mettre que les première lignes du tableau afin de simplifier la présentation)*

[caractère, Nb occurence, probabilité]

- [' ', 3971, 0.16616453259687003]

- ['e', 2860, 0.11967528663486485]

- ['s', 1666, 0.06971294669009959]

- ['n', 1416, 0.05925182023600301]

- ['a', 1297, 0.05427232404385304]

- ['t', 1264, 0.052891455351912295]

- ['i', 1203, 0.05033894049711273]

- ['u', 1187, 0.04966942840405055]

- ['r', 1174, 0.04912544982843753]

- ['o', 1022, 0.042765084944346804]

#### 3. Entropie de l'alphabée

Grace à ce tableau, et à notre code nous pouvons calculer l'entropie grace à la formule suivante : 

$$
H = \sum_i p(x_i)*log(\frac{1}{p(x_i)})
$$

```bash
L'entropie de notre alphabet est de :  4.3880255630216025
```

L'unité de notre entropie est : bits d'info/caractère.

#### 4. Taille du fichier en octets

#### 5. Algorithme de codage binaire

### II. Entroprie d'une image

#### 0. Introduction

#### 1. Code

Nous avons réutilisé le même algorithme qu'à la partie 1, en changeant juste la variable d'entrée de la fonction pour un tableau dans lequel chaque élément est une valeur de l'image RAW.

#### 2. Estimation de l'entropie et comparaison avec celle du texte

D'après nos calculs, l'entropie de l'image est d'environ 7,45.
