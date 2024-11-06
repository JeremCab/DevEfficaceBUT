import math
import random
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# (1) La classe ABR est exactement similaire à la classe arbre binaire.
# C'est à nous de vérifier la propriété en plus !

class ABR:
    def __init__(self, valeur, fils_gauche=None, fils_droit=None):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

# (2) Créez "à la main" deux ABR différents contenant les valeurs 1,2,3,4,5,6,7.
# (Indication : sur papier, insérer les valeurs dans un ordre aléatoire)

# arbre 1
a1 = ABR(1)
a3 = ABR(3)
a2 = ABR(2, a1, a3)
a5 = ABR(5)
a7 = ABR(7)
a6 = ABR(6, a5, a7)
arbre_1 = ABR(4, a2, a6)

# arbre 2
b1 = ABR(1)
b4 = ABR(4)
b3 = ABR(3, None, b4)
b2 = ABR(2, b1, b3)
b7 = ABR(7)
b6 = ABR(6, None, b7)
arbre_2 = ABR(5, b2, b6)


# (3) Complétez (parcours infixe !) ; on peut si on veut faire des méthodes,
# et soit afficher soit changer le nom et renvoyer une liste des valeurs.

def affichage_trie(abr):
    """
    Affiche les valeurs (print) dans l'ordre croissant.

    Args:
        abr (ABR): l'arbre
    """
    if abr is not None:
        affichage_trie(abr.fils_gauche)
        print(abr.valeur, end=" ")
        affichage_trie(abr.fils_droit)


print("\n")
print("Affichage")
affichage_trie(arbre_1)
print()
affichage_trie(arbre_2)


# (4) Recherche d'un élément (c'est dans le cours...)
def recherche(abr, val):
    """
    Cherche la valeur val dans l'ABR. Renvoie un Booléen.

    Args:
        abr (ABR): l'arbre
        val (int): valeur cherchée
    Returns:
        bool : indique si l'élément est dans l'arbre
    """
    if abr is None:
        return False

    elif abr.valeur == val:
        return True
    else:
        if val < abr.valeur:
            return recherche(abr.fils_gauche, val)
        else:
            return recherche(abr.fils_droit, val)


print("\n")
print("Recherche")
print(recherche(arbre_1, 6))
print(recherche(arbre_1, 0))
print(recherche(arbre_1, 12))


# (5) Insertion d'un élément
def insertion(abr, val):
    """
    Insère un nouveau noeud de valeur val dans l'ABR

    Args:
        abr (ABR): l'arbre dans lequel insérer
        val (int): valeur à insérer
    """
    if abr is None:
        return ABR(val)
    elif val < abr.valeur:
        abr.fils_gauche = insertion(abr.fils_gauche, val)
    else:
        abr.fils_droit = insertion(abr.fils_droit, val)
    return abr

print("\n")
print("Insertion")
arbre_1 = insertion(arbre_1, -2)
affichage_trie(arbre_1)
print()
arbre_1 = insertion(arbre_1, 3.5)
affichage_trie(arbre_1)
arbre_1 = insertion(arbre_1, 4.5)
affichage_trie(arbre_1)
arbre_1 = insertion(arbre_1, 5.5)
affichage_trie(arbre_1)
print()
arbre_1 = insertion(arbre_1, 12)
affichage_trie(arbre_1)
print()
a = None
a = insertion(a, 42)
affichage_trie(a)


# (6) Génération d'un arbre aléatoire
def arbre_aleatoire(valeurs):
    """
    Renvoie un ABR construit en insérant les valeurs de la liste
    dans un ordre aléatoire

    Args:
        valeurs ([int]): une liste de valeurs
    Returns:
        ABR
    """

    random.shuffle(valeurs)

    abr = None
    for k in valeurs:
        abr = insertion(abr, k)

    return abr


print("\n")
print("Arbres aléatoires")
a = arbre_aleatoire(list(range(-10, 11)))
affichage_trie(a)
print()
a = arbre_aleatoire(list(range(0, 101)))
affichage_trie(a)


# (7) À vous de faire : maximum, minimum, successeur et prédecesseur.
# Vous pouvez maintenant tester sur des arbres aléatoires contenant
# les valeurs 1...N, même pour de grandes valeurs de N !

def minimum(abr):
    """
    Renvoie le minimum (i.e., la clé minimale) d'un ABR.

    Args:
        abr (ABR): l'arbre en question
    Returns:
        min (int): clé minimale de abr
    """
    if abr is None:
        return None
    while abr.fils_gauche is not None:
        abr = abr.fils_gauche
    return abr.valeur


def maximum(abr):
    """
    Renvoie le maximum (i.e., la clé maximale) d'un ABR.

    Args:
        abr (ABR): l'arbre en question
    Returns:
        max (int): clé maximale de abr
    """
    if abr is None:
        return None
    while abr.fils_droit is not None:
        abr = abr.fils_droit
    return abr.valeur


print("\n")
print("Minimum")
print(minimum(arbre_1))
print(minimum(arbre_2))

print("\n")
print("Maximum")
print(maximum(arbre_1))
print(maximum(arbre_2))


def successeur(abr, val, succ=None):
    """
    Renvoie le successeur de val dans ABR,
    si ce dernier existe et None sinon.
    Renvoie None sinon.

    Remarque: une implémentation classique de cette fonction
    requiererait un attribut "parent" dans la class ABR...
    On palie ce problème en ajoutant le paramètre succ.

    Args:
        abr (ABR): l'arbre en question
        val (int): valeur dont il faut trouver le successeur
        succ (ABR): noeud successeur à ce stade de la recherche
    Returns:
        succ.valeur (int) : successeur de val
    """

    # cas de base
    # si le fils visité est None, on retourne le parent
    if abr is None:
        try:
            return succ.valeur
        except:
            return None

    # si un neud abr de valeur val existe,
    # et si abr possède un sous-arbre droit,
    # alors le successeur est le minimum de ce sous-arbre droit.
    if abr.valeur == val and abr.fils_droit:
        return minimum(abr.fils_droit)

    # si val < abr.valeur, on cherche récursivement dans le fils gauche de abr
    # tout en gardant en mémoire la racine de abr (le parent)
    elif val < abr.valeur:
        succ = abr
        return successeur(abr.fils_gauche, val, succ)

    # si val > abr.valeur, on cherche récursivement dans le fils droit de abr
    else:
        return successeur(abr.fils_droit, val, succ)


def predecesseur(abr, val, pred=None):
    """
    Renvoie le prédécesseur de val dans ABR.
    si ce dernier existe et None sinon.

    Args:
        abr (ABR): l'arbre en question
        val (int): valeur dont il faut trouver le successeur
        succ (ABR): noeud successeur à ce stade de la recherche
    Returns:
        succ.valeur (int) : successeur de val
    """

    # cas de base
    if abr is None:
        try:
            return pred.valeur
        except:
            return None

    # si un neud abr de valeur val existe,
    # et si abr possède un sous-arbre gauche,
    # alors le prédécesseur est le maximum de ce sous-arbre gauche.
    if abr.valeur == val and abr.fils_gauche:
        return maximum(abr.fils_gauche)

    # si val > abr.valeur, on cherche récursivement dans le fils droit de abr
    # tout en gardant en mémoire la racine de abr (le parent)
    elif val > abr.valeur:
        pred = abr
        return predecesseur(abr.fils_droit, val, pred)

    # si val < abr.valeur, on cherche récursivement dans le fils gauche de abr
    else:
        return predecesseur(abr.fils_gauche, val, pred)


print("\n")
print("Successeur")
for k in range(-5, 15):
    print(f"successeur de {k}:", successeur(arbre_1, k))

print("\n")
print("Prédécesseur")
for k in range(-5, 15):
    print(f"Prédécesseur de {k}:", predecesseur(arbre_1, k))


# (8) Expérience : pour diverses valeurs de N, générez un arbre aléatoire
# contenant les valeurs 1,2,...,N.
# Mesurez sa hauteur (se trouve dans le TP précédent).
# Répétez un grand nombre de fois pour obtenir une hauteur moyenne.
# Pour diverses valeurs de N, tracez le graphe
# des hauteurs moyennes en fonction de N.
# Comparez à la fonction math.log(N, 2).


def hauteur_arbre(arbre):

    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur_arbre(arbre.fils_gauche), \
                       hauteur_arbre(arbre.fils_droit))


hauteurs = []
nb_exp = 200
N_values = range(10, 200, 10)

for N in N_values:

    hauteur_moyenne = 0

    for exp in range(nb_exp):

        valeurs = list(range(N))
        a = arbre_aleatoire(valeurs)
        hauteur_moyenne += hauteur_arbre(a)

    hauteur_moyenne /= nb_exp
    hauteurs.append(hauteur_moyenne)


# formule Cormen p.261
# E[X_n] = log_2[(n^3 + 6^n2 + 11n + 6) / 24]
def f(n):
    return math.log((n**3 + 6*n**2 + 11*n + 6)/24, 2)
hauteurs_theoriques = [f(N) for N in N_values]


plt.figure(figsize=(10, 5))

x_values = list(range(len(N_values)))
plt.plot(x_values, hauteurs,
        linewidth=3, label="hauteurs moyennes")
plt.plot(x_values, hauteurs_theoriques,
        linewidth=3, label="hauteurs théoriques en $O(\log n)$\n\
$E[X_n] = \log [ (n^3 + 6n^2 + 11n + 6) / 24 ]$")
plt.xticks(x_values, N_values)
plt.xlabel("N")
plt.legend()

plt.show()
