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
    i, j, k = 0, 0, 0

    tab = [None] * (len(tab1) + len(tab2))

    while (i < len(tab1)) and (j < len(tab2)):

        if tab1[i] < tab2[j]:
            tab[k] = tab1[i]
            i += 1
        else:
            tab[k] = tab2[j]
            j += 1
        k += 1

    if i < len(tab1):
        tab[k:] = tab1[i:]

    elif j < len(tab2):
        tab[k:] = tab2[j:]

    return tab

def tri_fusion(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """
    if len(tab) <= 1:
        return tab
    else:
        tab1 = tri_fusion(tab[:len(tab)//2])
        tab2 = tri_fusion(tab[len(tab)//2:])
        return fusion_croissante(tab1, tab2)


def fusion_iterative(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    version itérative de la fusion

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """
    if len(tab) > 0:
        sous_tab = [[x] for x in tab]
    else:
        return tab
    while len(sous_tab) >= 2:
         sous_tab.append(fusion_croissante(sous_tab.pop(0),
                                           sous_tab.pop(0)))
    return sous_tab[0]

def sous_tableaux_monotones(tab):
    """renvoie une liste des sous-tableaux monotones qui constituent tab

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : liste de list (sous-tableaux)
    """

    result = [[]]

    for e in tab:

        sous_tab = result[-1]

        # si monotone, on remplit le sous-tableau
        if len(sous_tab) <= 1 or (e - sous_tab[-1]) * (sous_tab[-1] - sous_tab[-2]) > 0:
            sous_tab.append(e)

        # si non-monotone, on rajoute le sous-tableau et on en crée un nouveau
        else:
            if sous_tab[-2] > sous_tab[-1]: # si décroissant, on permute
                sous_tab.reverse()

            result.append([e])

    # dernier sous-tableau
    if len(result[-1]) <= 1 or result[-1][-2] > result[-1][-1]:
        result[-1].reverse()

    return result

def timsort(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    procède itérativement comme la fusion en utilisant les sous-tableaux monotones

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """

    sous_tab = sous_tableaux_monotones(tab)

    while len(sous_tab) >= 2:
         sous_tab.append(fusion_croissante(sous_tab.pop(0), sous_tab.pop(0)))

    return sous_tab[0]


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

                tmp = fusion_iterative(a_trier)
                self.assertEqual(tmp, croissante)

                tmp = timsort(a_trier)
                self.assertEqual(tmp, croissante)

if __name__ == '__main__':
    unittest.main()
