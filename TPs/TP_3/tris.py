########################################
# TP dev efficace semaine 2            #
# TRIS                                 #
########################################


import itertools
import unittest
#from collections import deque


def fusion_croissante(tab1, tab2):
    """renvoie un tableau croissant, résultat de la fusion
    des tableaux croissants tab1 et tab2

    Args:
        tab1 (list): tableaux croissant
        tab2 (list): tableaux croissant

    Returns:
        list : nouveau tableau croissant
    """

    # à compléter
    pass

def tri_fusion(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """

    # à compléter
    pass


def fusion_iterative(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    version itérative de la fusion

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """

    # à compléter
    pass

def sous_tableaux_monotones(tab):
    """renvoie une liste des sous-tableaux monotones qui constituent tab

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : liste de list (sous-tableaux)
    """

    # à compléter
    pass

def timsort(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    procède itérativement comme la fusion en utilisant les sous-tableaux monotones

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """

    # à compléter
    pass

class TestFusion(unittest.TestCase):

    def test_fusion_croissante(self):

        tab = fusion_croissante([1,2],[1,2,3])
        self.assertEqual(tab,[1,1,2,2,3])
        tab = fusion_croissante([],[1,2,3])
        self.assertEqual(tab,[1,2,3])
        tab = fusion_croissante([],[])
        self.assertEqual(tab,[])

    def test_tri_fusion(self):
        #on va tester sur tous les ordres possibles pour N de 1 à 8
        for N in range(8):
            croissante = list(range(N))
            for p in itertools.permutations(croissante):
                a_trier = list(p)
                tmp = tri_fusion(a_trier)
                self.assertEqual(tmp, croissante)

                # à compléter...

if __name__ == '__main__':
    unittest.main()
