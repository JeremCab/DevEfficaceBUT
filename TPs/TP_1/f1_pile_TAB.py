########################################
# TP dev efficace semaine 1            #
# implementation pile LIFO par tableau #
########################################


import unittest

"""
On fournit le début de classe suivante pour implémenter une pile
par un tableau. On utilisera un tableau statique dans la mémoire ayant
une taille N fixée au départ (on évite donc d'utiliser append)
Complétez les méthodes !
"""

class Pile_tab:
    def __init__(self, N):
        """creation de la pile

        Args:
            N (int): taille max de la pile
        """
        self.tab = [None]*N
        self.sommet = -1 # indice du dernier element entré

    def est_vide(self):
        """renvoie un booléen indiquant si la pile est vide
        """

        #TODO
        pass

    def est_pleine(self):
        """renvoie un booléen indiquant si la pile est pleine
        """


        #TODO
        pass

    def empiler(self, x):
        """ajoute x au sommet de la pile

        Args:
            x : élément à empiler

        Raises:
            Exception: indique que la pile est pleine
        """

        if self.est_pleine():
            raise Exception("La pile est pleine !")
        else:

            #TODO
            pass


    def depiler(self):
        """renvoie et supprime l'élément au sommet de la pile

        Raises:
            Exception: indique que la pile est vide
        """

        if self.est_vide():
            raise Exception("La pile est vide !")
        else:

            #TODO
            pass

class TestPile(unittest.TestCase):

    def test_vide(self):
        for N in [0,1,2,5,10,100]:
            p = Pile_tab(N)
            self.assertTrue(p.est_vide())

    def test_empiler_et_pleine(self):
        for N in [0,1,2,5,10,100]:
            p = Pile_tab(N)
            for i in range(N):
                p.empiler(i)
                self.assertEqual(p.sommet,i)
            with self.assertRaises(BaseException) :
                p.empiler(0)

    def test_depiler(self):
        for N in [0,1,2,5,10,100]:
            p = Pile_tab(N)
            with self.assertRaises(BaseException) :
                p.depiler()
            for i in range(N//2):
                p.empiler(i)
            for i in range(N//2):
                self.assertEqual(p.depiler(),N//2-1-i)

    def test_scenario_complet(self):
        p = Pile_tab(5)
        self.assertTrue(p.est_vide())
        for i in range(5):
            p.empiler(i)
        self.assertTrue(p.est_pleine())
        with self.assertRaises(BaseException) :
            p.empiler(0)
        self.assertEqual(p.depiler(),4)
        self.assertEqual(p.depiler(),3)
        self.assertEqual(p.depiler(),2)
        p.empiler(5)
        p.empiler(6)
        self.assertEqual(p.depiler(),6)
        self.assertEqual(p.depiler(),5)
        self.assertEqual(p.depiler(),1)
        self.assertEqual(p.depiler(),0)
        with self.assertRaises(BaseException):
            p.depiler()



if __name__ == '__main__':
    unittest.main()
