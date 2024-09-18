###########################################
# TP dev efficace semaine 1               #
# implementation file FIFO liste chaînée  #
###########################################



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

class File_LC:
    def __init__(self):
        """création file vide
        """

        self.entrée = None #dernier maillon de la liste, où on fait les ajouts
        self.sortie = None #premier maillon de la liste, prêt à sortir


""" 
A vous d'écrire les méthodes de la file ainsi que les tests !
"""