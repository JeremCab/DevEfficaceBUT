
#1) Comprendre la classe arbre binaire

class Arbre_binaire:
    def __init__(self, valeur, fils_gauche, fils_droit):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

#2) Créez à la main un abre contenant les valeurs (oui c'est pénible mais faut savoir le faire)
"""
         'A'
     'B'     'C'
  'D'  'E'  . 'F'
'G' . 'H'.    .  'I'
. .   . .         . .
le . signifie qu'il n'y a pas de fils
"""

fg = Arbre_binaire('G',None,None)
fh = Arbre_binaire('H',None,None)
fi = Arbre_binaire('I',None,None)

a1 = Arbre_binaire('A', \
    Arbre_binaire('B', Arbre_binaire('D',fg,None), Arbre_binaire('E',fh,None)), \
    Arbre_binaire('C', None, Arbre_binaire('F',None,fi)))


#3) complétez les 3 fonctions d'affichage et testez

def affiche_ordre_prefixe(arbre):
    if arbre:
        print(arbre.valeur, end = " ")
        affiche_ordre_prefixe(arbre.fils_gauche)
        affiche_ordre_prefixe(arbre.fils_droit)

def affiche_ordre_suffixe(arbre):
     if arbre:
        affiche_ordre_suffixe(arbre.fils_gauche)
        affiche_ordre_suffixe(arbre.fils_droit)
        print(arbre.valeur, end = " ")

def affiche_ordre_infixe(arbre):
    if arbre:
        affiche_ordre_infixe(arbre.fils_gauche)
        print(arbre.valeur, end = " ")
        affiche_ordre_infixe(arbre.fils_droit)


#tests
affiche_ordre_prefixe(a1) ; print()
affiche_ordre_suffixe(a1) ; print()
affiche_ordre_infixe(a1) ; print()


#4) et le parcours en largeur ?

def affiche_ordre_largeur(arbre):
    if not arbre:
        return
    attente = [arbre]
    while attente:
        courant = attente.pop(0)
        print(courant.valeur, end = " ")
        if courant.fils_gauche:
            attente.append(courant.fils_gauche)
        if courant.fils_droit:
            attente.append(courant.fils_droit)

affiche_ordre_largeur(a1)
print()

#5) Complétez les fonction:

def nb_noeuds(arbre):
    if not arbre:
        return 0
    else:
        return 1 + nb_noeuds(arbre.fils_gauche) + nb_noeuds(arbre.fils_droit)

print(nb_noeuds(a1))

def hauteur_arbre(arbre):
    if not arbre:
        return 0
    else:
        return 1 + max(hauteur_arbre(arbre.fils_gauche), hauteur_arbre(arbre.fils_droit))
print(hauteur_arbre(a1))

def max_valeurs_arbre(arbre):
    if not arbre:
        return "" # plus petit que les caractères
    else:
        return max(arbre.valeur, max_valeurs_arbre(arbre.fils_gauche), max_valeurs_arbre(arbre.fils_droit))
print(max_valeurs_arbre(a1))

#6) complétez cette fonction qui convertit un arbre binaire en un tableau
#reponse pour l'arbre ci-dessus [None,'A','B','C','D','E',None,'F','G',None,'H',None,None,none,'I']

def arbre_binaire_vers_tableau(arbre):
    #le plus simple est de refaire un parcours largeur
    tab = []
    attente = [arbre]
    while attente:
        courant = attente.pop(0)
        if courant:
            tab.append(courant.valeur)
        else:
            tab.append(None)
        if courant:
            attente.append(courant.fils_gauche)
            attente.append(courant.fils_droit)
    return tab

tab1 = arbre_binaire_vers_tableau(a1)
print(tab1)

#6.5) Et l'inverse ?

def tableau_vers_arbre_binaire(tab, racine = 1):
    if racine >= len(tab) or tab[racine]==None:
        return None
    fg = tableau_vers_arbre_binaire(tab, 2*racine)
    fd = tableau_vers_arbre_binaire(tab, 2*racine + 1)
    return Arbre_binaire(tab[racine], fg, fd)

print(affiche_ordre_largeur(tableau_vers_arbre_binaire(tab1)))

################################################
# Application : expressions arithmétiques      #
################################################

"""
On stocke dans un arbre binaire des expressions comme 2 + 5*(7+5)
Les noeuds internes de l'arbre une une valeur '+' ou '-' ou '*' ou '//'
Les feuilles ont pour valeur un entier et donc NE SONT PAS DES  OBJETS Arbre_binaire
"""
#7) Créer l'arbre binaire correspondant à 2 + 5*(1 + 10//(7-3))

a2 = Arbre_binaire('+', 2, \
        Arbre_binaire('*', 5, \
            Arbre_binaire('+', 1, \
                Arbre_binaire('//',10, \
                    Arbre_binaire('-',7,3)))))

#8) Ecrire une fonction qui évalue la valeur d'un arbre binaire d'expression arithmétique

def evaluer(arbre):

    if isinstance(arbre, int):
        return arbre
        
    else:
        print(arbre.valeur)
        if arbre.valeur == '+':
            return evaluer(arbre.fils_gauche) + evaluer(arbre.fils_droit)
        elif arbre.valeur == '-':
            return evaluer(arbre.fils_gauche) - evaluer(arbre.fils_droit)
        elif arbre.valeur == '*':
            return evaluer(arbre.fils_gauche) * evaluer(arbre.fils_droit)
        elif arbre.valeur == '//':
            return evaluer(arbre.fils_gauche) // evaluer(arbre.fils_droit)

print(evaluer(a2))

#9) Si vous êtes en forme, écrivez une fonction qui parse une str comme "2 + 5*(1 + 10//(7-3))" et crée l'arbre binaire associé
#...
