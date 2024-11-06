import math
import random
import matplotlib.pyplot as plt


# (1) La classe ABR est exactement similaire à la classe arbre binaire.
# C'est à nous de vérifier la propriété en plus !

class ABR:
    def __init__(self, valeur, fils_gauche=None, fils_droit=None):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

# (2) Créez "à la main" deux ABR différents contenant les valeurs 1,2,3,4,5,6,7.
# (Indication : sur papier, insérer les valeurs dans un ordre aléatoire)

a1 = ABR(1)
a3 = ABR(3)
a2 = ABR(2, a1, a3)
a5 = ABR(5)
a7 = ABR(7)
a6 = ABR(6, a5, a7)
abr1 = ABR(4, a2, a6)

b1 = ABR(1)
b3 = ABR(3)
b2 = ABR(2, b1, b3)
b7 = ABR(7)
b6 = ABR(6, None, b7)
b5 = ABR(5, None, b6)
abr2 = ABR(4, b2, b5)


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


print("\naffichage arb1")
affichage_trie(abr1)
print("\naffichage arb2")
affichage_trie(abr2)



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
for i in [-1, 2, 3, 12]:
    print(f"rechercher {i}:", recherche(abr1, i))



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

print("")
for i in [-3, -7, 44, 21, -12, 9]:
    print(f"Insérer {i}")
    insertion(abr1, i)

print("\nNouvel arbre:")
affichage_trie(abr1)


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

    abr = None
    random.shuffle(valeurs)

    for x in valeurs:
        abr = insertion(abr, x)

    return abr

print("\n\nArbre aléatoire:")
abr_aleatoire = arbre_aleatoire(list(range(45)))
affichage_trie(abr_aleatoire)


# (7) À vous de faire : maximum, minimum, successeur et prédecesseur.
# Vous pouvez maintenant tester sur des arbres aléatoires contenant
# les valeurs 1...N, même pour de grandes valeurs de N !

def minimum(abr):

    while abr.fils_gauche is not None:
        abr = abr.fils_gauche

    return abr.valeur

print("")
print("\nMinimium", minimum(abr1))
print("Minimium", minimum(abr2))
print("Minimium", minimum(abr_aleatoire))


def maximum(abr):

    while abr.fils_droit is not None:
        abr = abr.fils_droit

    return abr.valeur

print("")
print("\nMaximum", maximum(abr1))
print("Maximum", maximum(abr2))
print("Maximum", maximum(abr_aleatoire))


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
    print(f"successeur de {k}:", successeur(abr1, k))

print("\n")
print("Prédécesseur")
for k in range(-5, 15):
    print(f"Prédécesseur de {k}:", predecesseur(abr1, k))



# (8) Expérience : pour diverses valeurs de N, générez un arbre aléatoire
# contenant les valeurs 1,2,...,N.
# Mesurez sa hauteur (se trouve dans le TP précédent).
# Répétez un grand nombre de fois pour obtenir une hauteur moyenne.
# Pour diverses valeurs de N, tracez le graphe
# des hauteurs moyennes en fonction de N.
# Comparez à la fonction math.log(N, 2).

def hauteur(abr):
    if abr is None:
        return 0
    else:
        return 1+max(hauteur(abr.fils_gauche), hauteur(abr.fils_droit))

nb_exp = 1000
h_moyennes_l = []

for n in range(1, 50):
    h_moyenne = 0
    for i in range(nb_exp):
        a = arbre_aleatoire(list(range(n)))
        h_moyenne += hauteur(a)
    h_moyenne /= nb_exp
    h_moyennes_l.append(h_moyenne)


plt.figure(figsize=(12, 6))
plt.plot(range(1, 50), h_moyennes_l, label="hauteurs moyennes", linewidth=3)
plt.plot(range(1, 50), [math.log(x, 2) for x in range(1, 50)], label="$\log_2(n)$", linewidth=3)
plt.legend()
plt.show()
