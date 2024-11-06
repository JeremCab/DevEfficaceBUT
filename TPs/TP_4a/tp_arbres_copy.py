
# (1) Comprendre la classe arbre binaire

class Arbre_binaire:

    def __init__(self, valeur, fils_gauche, fils_droit):

        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

# (2) Créez à la main un abre contenant les valeurs
"""
         'A'
     'B'     'C'
  'D'  'E'  . 'F'
'G' . 'H'.    .  'I'
. .   . .         . .
le . signifie qu'il n'y a pas de fils
"""
g = Arbre_binaire("G", None, None)
h = Arbre_binaire("H", None, None)
i = Arbre_binaire("I", None, None)
d = Arbre_binaire("D", g, None)
e = Arbre_binaire("E", h, None)
f = Arbre_binaire("F", None, i)
b = Arbre_binaire("B", d, e)
c = Arbre_binaire("C", None, f)
a = Arbre_binaire("A", b, c)


# (3) complétez les 3 fonctions d'affichage et testez

def affiche_ordre_prefixe(arbre):
    if arbre is not None:
        print(arbre.valeur, end=" ")
        affiche_ordre_prefixe(arbre.fils_gauche)
        affiche_ordre_prefixe(arbre.fils_droit)

def affiche_ordre_suffixe(arbre):
    if arbre is not None:
        affiche_ordre_suffixe(arbre.fils_gauche)
        affiche_ordre_suffixe(arbre.fils_droit)
        print(arbre.valeur, end=" ")


def affiche_ordre_infixe(arbre):
    if arbre is not None:
        affiche_ordre_infixe(arbre.fils_gauche)
        print(arbre.valeur, end=" ")
        affiche_ordre_infixe(arbre.fils_droit)

print("\nParcours préfixe:")
affiche_ordre_prefixe(a)
print("\nParcours suffixe:")
affiche_ordre_suffixe(a)
print("\nParcours infixe:")
affiche_ordre_infixe(a)

# (4) et le parcours en largeur ?

def affiche_ordre_largeur(arbre):
    file = [arbre]
    while file != []:
        courant = file.pop(0) # FIFO
        print(courant.valeur, end=" ")
        if courant.fils_gauche is not None:
            file.append(courant.fils_gauche)
        if courant.fils_droit is not None:
            file.append(courant.fils_droit)

print("\nParcours en largeur:")
affiche_ordre_largeur(a)

# (5) Complétez les fonction:

def nb_noeuds(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + nb_noeuds(arbre.fils_gauche) + nb_noeuds(arbre.fils_droit)

print(f"\nNb noeud: {nb_noeuds(a)}")

def hauteur_arbre(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur_arbre(arbre.fils_gauche), \
        hauteur_arbre(arbre.fils_droit))

print(f"Hauteur: {hauteur_arbre(a)}")

def max_valeurs_arbre(arbre):
    if arbre is None:
        return ""
    else:
        return max(arbre.valeur, \
        max_valeurs_arbre(arbre.fils_gauche), \
        max_valeurs_arbre(arbre.fils_droit))

print(f"Recherche maximum: {max_valeurs_arbre(a)}")


# (6) complétez cette fonction qui convertit un arbre binaire en un tableau
# réponse pour l'arbre ci-dessus [None,'A','B','C','D','E',None,'F','G',None,'H',None,None,none,'I']

def arbre_binaire_vers_tableau(arbre):
    tab = []
    file = [arbre]
    while file != []:
        courant = file.pop(0) # FIFO
        if courant is not None:
            tab.append(courant.valeur)
            file.append(courant.fils_gauche)
            file.append(courant.fils_droit)
        else:
            tab.append(courant)
    return tab

tab = arbre_binaire_vers_tableau(a)
print(f"Arbre vers tableau: {tab}")

# Et l'inverse ?

def tableau_vers_arbre_binaire(tab, racine=0):
    if racine >= len(tab) or tab[racine]==None:
        return None
    fg = tableau_vers_arbre_binaire(tab, 2*racine+1)
    fd = tableau_vers_arbre_binaire(tab, 2*racine+2)
    return Arbre_binaire(tab[racine], fg, fd)

a2 = tableau_vers_arbre_binaire(tab)
print("Tableau vers arbre:")
affiche_ordre_largeur(a2)

################################################
# Application : expressions arithmétiques      #
################################################

"""
On stocke dans un arbre binaire des expressions comme 2 + 5*(7+5)
Les noeuds internes de l'arbre ont une valeur '+' ou '-' ou '*' ou '//'
Les feuilles ont pour valeur un entier
"""
# (7) Créer l'arbre binaire correspondant à 2 + 5*(1 + 10//(7-3))


# (8) Ecrire une fonction qui évalue la valeur d'un arbre binaire d'expression arithmétique


# (9) Si vous êtes en forme, écrivez une fonction qui parse une str comme "2 + 5*(1 + 10//(7-3))" et crée l'arbre binaire associé
