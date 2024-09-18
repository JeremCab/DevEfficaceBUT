########################################
# TP dev efficace semaine 1            #
# implementation file FIFO par tableau #
########################################


import unittest


"""
C'est maintenant la structure de file FIFO que l'on veut implémenter
dans un tableau.
On maintient deux indices :
    - entrée, qui est l'indice où sera rangé le prochain élément à entrer
    - sortie, qui est l'indice où sera extrait le nouvel élément
A chaque entrée ou sortie les indices augmentent de 1, de façon circulaire
(au moment de passer à N, l'indice revient à 0)
On convient que si le tableau a une longueur N, on ne stocke que N-1 élément,
ceci afin de distinguer les cas
    - entrée == sortie : file vide
    - sortie = entrée + 1 (mod N) où la file est pleine
"""


class File_tab:

    def __init__(self, N):
        """creation de la file

        Args:
            N (int): taille du tableau, la taille de file est N-1
        """
        self.tab = [None]*N
        self.entree = 0 # indice du prochain élément à entrer
        self.sortie = 0 # indice du prochain élément à sortir

    def est_vide(self):
        """renvoie un booléen indiquant si la file est vide
        """
        return self.entree == self.sortie

    def est_pleine(self):
        """renvoie un booléen indiquant si la file est pleine
        """
        return self.sortie == (self.entree + 1)%len(self.tab)

    def enfiler(self, x):
        """ajoute x en queue de file

        Args:
            x : élément à enfiler

        Raises:
            Exception: indique que la file est pleine
        """
        if self.est_pleine():
            raise Exception("La file est pleine !")
        else:
            self.tab[self.entree] = x
            self.entree += 1
            self.entree %= len(self.tab)

    def defiler(self):
        """renvoie et supprime l'élément en tête de file

        Raises:
            Exception: indique que la file est vide
        """
        if self.est_vide():
            raise Exception("La file est vide !")
        else:
            x = self.tab[self.sortie]
            self.sortie += 1
            self.sortie %= len(self.tab)
            return x

class TestFile(unittest.TestCase):

    def test_vide(self):
        # tableau de taille minimum 1 pour stocker une file vide
        for N in [1, 2, 5, 10, 100]:
            f = File_tab(N)
            self.assertTrue(f.est_vide())

    def test_enfiler_et_pleine(self):
        for N in [1, 2, 5, 10, 100]:
            f = File_tab(N)
            for i in range(N-1): # seulement N-1 éléments
                f.enfiler(i)
                self.assertEqual(f.entree, i+1)
            with self.assertRaises(BaseException) :
                f.enfiler(0)

    def test_defiler(self):
        for N in [1, 2, 5, 10, 100]:
            f = File_tab(N)
            with self.assertRaises(BaseException) :
                f.defiler()
            for i in range(N//2):
                f.enfiler(i)
            for i in range(N//2):
                # si file vide, pas possible d'enfiler, donc de defiler
                if N == 1:
                    with self.assertRaises(BaseException) :
                        f.defiler()
                else:
                    self.assertEqual(f.defiler(), i)

    def test_scenario_complet(self):
        f = File_tab(6) # longueur 6 pour 5 éléments
        self.assertTrue(f.est_vide())
        for i in range(5):
            f.enfiler(i)
        self.assertTrue(f.est_pleine())
        with self.assertRaises(BaseException) :
            f.enfiler(0)
        self.assertEqual(f.defiler(), 0)
        self.assertEqual(f.defiler(), 1)
        self.assertEqual(f.defiler(), 2)
        f.enfiler(123)
        self.assertEqual(f.defiler(), 3)
        self.assertEqual(f.defiler(), 4)
        self.assertEqual(f.defiler(), 123)
        self.assertTrue(f.est_vide())
        with self.assertRaises(BaseException) :
            p.defiler()


if __name__ == '__main__':
    unittest.main()
