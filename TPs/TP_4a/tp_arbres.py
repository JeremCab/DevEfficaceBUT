
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


# (3) complétez les 3 fonctions d'affichage et testez

def affiche_ordre_prefixe(arbre):
    pass

def affiche_ordre_suffixe(arbre):
    pass

def affiche_ordre_infixe(arbre):
    pass

# (4) et le parcours en largeur ?

def affiche_ordre_largeur(arbre):
    pass

# (5) Complétez les fonction:

def nb_noeuds_(arbre):
    pass

def hauteur_arbre(arbre):
    pass

def max_valeurs_arbre(arbre):
    pass

# (6) complétez cette fonction qui convertit un arbre binaire en un tableau
# réponse pour l'arbre ci-dessus [None,'A','B','C','D','E',None,'F','G',None,'H',None,None,none,'I']

def arbre_binaire_vers_tableau(arbre):
    pass

# Et l'inverse ?

def tableau_vers_arbre_binaire(tab):
    pass

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
