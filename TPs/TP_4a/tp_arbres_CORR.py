# (1) Comprendre la classe arbre binaire

class Arbre_binaire:

    def __init__(self, valeur, fils_gauche, fils_droit):

        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

# Structure de données récursive :
# un arbre bianaire est un noeud dont les fils gauche et droit
# aont eux-mêmes des arbres binaires (possiblement vides).


# (2) Créez à la main un abre contenant les valeurs
"""
         'A'
     'B'     'C'
  'D'  'E'  . 'F'
'G' . 'H'.    .  'I'
. .   . .         . .
le . signifie qu'il n'y a pas de fils
"""
# on construit l'arbre de bas en haut
# feuilles
g = Arbre_binaire("G", None, None)
h = Arbre_binaire("H", None, None)
i = Arbre_binaire("I", None, None)
# niveau h-1
d = Arbre_binaire("D", g, None)
e = Arbre_binaire("E", h, None)
f = Arbre_binaire("F", None, i)
# niveau h-2
b = Arbre_binaire("B", d, e)
c = Arbre_binaire("C", None, f)
# racine
arbre = Arbre_binaire("A", b, c)

# # racine
# print(arbre.valeur)
# # level 1
# print(arbre.fils_gauche.valeur)
# print(arbre.fils_droit.valeur)
# # level 2
# print(arbre.fils_gauche.fils_gauche.valeur)
# print(arbre.fils_gauche.fils_droit.valeur)
# # print(arbre.fils_droit.fils_gauche.valeur)
# print(arbre.fils_droit.fils_droit.valeur)
# # level 3
# print(arbre.fils_gauche.fils_gauche.fils_gauche.valeur)
# #print(arbre.fils_gauche.fils_gauche.fils_droit.valeur)
# print(arbre.fils_gauche.fils_droit.fils_gauche.valeur)
# #print(arbre.fils_gauche.fils_droit.fils_droit.valeur)
# #print(arbre.fils_droit.fils_gauche.fils_gauche.valeur)
# #print(arbre.fils_droit.fils_gauche.fils_droit.valeur)
# #print(arbre.fils_droit.fils_droit.fils_gauche.valeur)
# print(arbre.fils_droit.fils_droit.fils_droit.valeur)


# (3) complétez les 3 fonctions d'affichage et testez

def affiche_ordre_prefixe(arbre):
    if arbre is not None:
        print(arbre.valeur, end = " ")
        affiche_ordre_prefixe(arbre.fils_gauche)
        affiche_ordre_prefixe(arbre.fils_droit)

def affiche_ordre_suffixe(arbre):
    if arbre is not None:
        affiche_ordre_suffixe(arbre.fils_gauche)
        affiche_ordre_suffixe(arbre.fils_droit)
        print(arbre.valeur, end = " ")

def affiche_ordre_infixe(arbre):
    if arbre is not None:
        affiche_ordre_infixe(arbre.fils_gauche)
        print(arbre.valeur, end = " ")
        affiche_ordre_infixe(arbre.fils_droit)

print("\nAffichage préfixe")
affiche_ordre_prefixe(arbre)
print("\nAffichage suffixe")
affiche_ordre_suffixe(arbre)
print("\nAffichage infixe")
affiche_ordre_infixe(arbre)


# (4) et le parcours en largeur ?
# Idée: on utilise une file FIFO
# file = [arbre]
# tant que file != []:
#   noeud courant n = file.pop(0)
#   imprimer n
#   ajouter fils gauche puis droit de n dans la file s'ils existent

def affiche_ordre_largeur(arbre):

    if not arbre:
        return

    attente = [arbre]

    while attente:

        courant = attente.pop(0) # FIFO
        print(courant.valeur, end = " ")

        if courant.fils_gauche:
            attente.append(courant.fils_gauche)

        if courant.fils_droit:
            attente.append(courant.fils_droit)

print("\nAffichage largeur")
affiche_ordre_largeur(arbre)


# (5) Complétez les fonction:
# Idée: utiliser la récursivité

def nb_noeuds(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + nb_noeuds(arbre.fils_gauche) + \
                   nb_noeuds(arbre.fils_droit)

def hauteur_arbre(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur_arbre(arbre.fils_gauche), \
                       hauteur_arbre(arbre.fils_droit))

def max_valeurs_arbre(arbre):
    if not arbre:
        return "" # plus petit que les caractères
    else:
        return max(arbre.valeur, \
                   max_valeurs_arbre(arbre.fils_gauche), \
                   max_valeurs_arbre(arbre.fils_droit))

print()
print("\nNombre de noeuds")
print(nb_noeuds(arbre))
print("Hauteur")
print(hauteur_arbre(arbre))
print("Valeur maximale")
print(max_valeurs_arbre(arbre))


# (6) complétez cette fonction qui convertit un arbre binaire en un tableau
# Réponse pour l'arbre ci-dessus:
# [None,'A','B','C','D','E',None,'F','G',None,'H',None,None,None,'I']
# Le plus simple est de refaire un parcours largeur
# et d'ajouter les éléments dans le tableau au fur et à mesure

def arbre_binaire_vers_tableau(arbre):

    tab = []
    attente = [arbre]

    while attente:

        courant = attente.pop(0)

        if courant is not None:
            tab.append(courant.valeur)
            attente.append(courant.fils_gauche)
            attente.append(courant.fils_droit)

        else:
            tab.append(None)

    return tab

def arbre_binaire_vers_tableau2(arbre):

    tab = []
    attente = [arbre]

    while attente:

        courant = attente.pop(0)

        if courant is not None:
            tab.append(courant.valeur)
            attente.append(courant.fils_gauche)
            attente.append(courant.fils_droit)

        else:
            tab.append(None)

    return tab


print()
print("Tableau associé à l'arbre de départ")
tab = arbre_binaire_vers_tableau2(arbre)
print(tab)

# Et l'inverse ?

def tableau_vers_arbre_binaire(tab, racine = 0):

    if racine >= len(tab) or tab[racine] == None:
        return None

    else:
        fg = tableau_vers_arbre_binaire(tab, 2*racine + 1)
        fd = tableau_vers_arbre_binaire(tab, 2*racine + 2)

        return Arbre_binaire(tab[racine], fg, fd)

print("Arbre associé au tableau")
a = tableau_vers_arbre_binaire(tab)
print(affiche_ordre_largeur(a))


################################################
# Application : expressions arithmétiques      #
################################################

"""
On stocke dans un arbre binaire des expressions comme 2 + 5 * (7 + 5)
Les noeuds internes de l'arbre ont une valeur '+' ou '-' ou '*' ou '//'
Les feuilles ont pour valeur un entier
"""

# (7) Créer l'arbre binaire correspondant à:
# 2 + 5 * (1 + 10 // (7 - 3))

v2 = Arbre_binaire(2, None, None)
v5 = Arbre_binaire(5, None, None)
v1 = Arbre_binaire(1, None, None)
v10 = Arbre_binaire(10, None, None)
v7 = Arbre_binaire(7, None, None)
v3 = Arbre_binaire(3, None, None)

moins = Arbre_binaire("-", v7, v3)
divise = Arbre_binaire("//", v10, moins)
plus_1 = Arbre_binaire("+", v1, divise)
multiplie = Arbre_binaire("*", v5, plus_1)
final = Arbre_binaire("+", v2, multiplie)

print("\nAffichage préfixe")
affiche_ordre_prefixe(final)
print("\nAffichage suffixe")
affiche_ordre_suffixe(final)
print("\nAffichage infixe") # plus lisible
affiche_ordre_infixe(final)
print("\nAffichage largeur")
affiche_ordre_largeur(final)


# (8) Ecrire une fonction qui évalue la valeur
# d'un arbre binaire d'expression arithmétique

def evaluer(arbre):

    if isinstance(arbre.valeur, int):
        return arbre.valeur

    elif arbre.valeur == '+':
        return evaluer(arbre.fils_gauche) + evaluer(arbre.fils_droit)

    elif arbre.valeur == '-':
        return evaluer(arbre.fils_gauche) - evaluer(arbre.fils_droit)

    elif arbre.valeur == '*':
        return evaluer(arbre.fils_gauche) * evaluer(arbre.fils_droit)

    elif arbre.valeur == '//':
        return evaluer(arbre.fils_gauche) // evaluer(arbre.fils_droit)

print("\nEvaluation de l'expression: 2 + 5 * (1 + 10 // (7 - 3))")
print("Résultat:", evaluer(final))

# (9) Si vous êtes en forme, écrivez une fonction qui parse une str comme "2 + 5*(1 + 10//(7-3))" et crée l'arbre binaire associé
