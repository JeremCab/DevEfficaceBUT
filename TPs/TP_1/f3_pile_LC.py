##########################################
# TP dev efficace semaine 1              #
# implementation pile par liste chaînée  #
##########################################



import unittest


class Cellule:
    def __init__(self, valeur, suivante):
        """création d'une cellule

        Args:
            valeur (quelconque): la valeur à stocker dans la cellule
            suivante (Cellule): la cellule suivante de la liste chaînée
        """
        self.valeur = valeur
        self.suivante = suivante

class Pile:
    def __init__(self):
        """création d'une pile vide
        """
        self.sommet = None #le haut de la pile

""" 
A vous d'écrire les méthodes de la pile ainsi que les tests !
"""