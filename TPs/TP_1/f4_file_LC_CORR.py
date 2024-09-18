###########################################
# TP dev efficace semaine 1               #
# implementation file FIFO liste chaînée  #
###########################################



import unittest


class Cellule:

    def __init__(self, valeur, suivante=None):
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
        self.entree = None  # dernier maillon de la liste, où on fait les ajouts
        self.sortie = None  # premier maillon de la liste, prêt à sortir

    def est_vide(self):
        """renvoie un booléen indiquant si la file est vide
        """
        return self.sortie is None

    def enfiler(self, x):
        """ajoute x à l'entrée (i.e. fin!) de la file

        Args:
            x : élément à enfiler

        """
        # on enfile en ajoutant un élément en fin de liste O(1)
        if self.est_vide():           # si pile vide, x devient nouvelle sortie
            self.sortie = x
        else:
            self.entree.suivante = x  # mise à jour pointeur x
        self.entree = x               # x devient nouvelle entree

    def defiler(self):
        """renvoie et supprime l'élément à la sortie (i.e. début!) de la file

        Raises:
            Exception: indique que la file est vide
        """
        # on défile en supprimant l'élément en début de liste O(1)
        if self.est_vide():
            raise Exception("La file est vide !")
        else:
            x = self.sortie
            self.sortie = x.suivante
            return x


class TestFile_LC(unittest.TestCase):

    def test_vide(self):
        """unittests pour pile_vide
        """
        f = File_LC()
        self.assertTrue(f.est_vide())

    def test_enfiler(self):
        """unittests pour enfiler
        """
        f = File_LC()
        valeurs = [1, 5, 33, 27, -14]

        for v in valeurs:
            f.enfiler(Cellule(v))
            self.assertEqual(f.entree.valeur, v)

    def test_defiler(self):
        """unittests pour defiler
        """
        f = File_LC()
        valeurs = [1, 5, 33, 27, -14]

        for v in valeurs:
            f.enfiler(Cellule(v))

        for i in range(len(valeurs)):
            x = f.defiler()
            self.assertEqual(x.valeur, valeurs[i])

        with self.assertRaises(BaseException):  # file vide
            f.defiler()
        with self.assertRaises(BaseException):  # file vide
            f.defiler()

    def test_scenario_complet(self):
        """unittests pour un scenario complet
        """
        # pile vide
        f = File_LC()
        self.assertTrue(f.est_vide())

        # empilements
        f.enfiler(Cellule(12))
        self.assertEqual(f.entree.valeur, 12)
        f.enfiler(Cellule(3))
        f.enfiler(Cellule(47))
        self.assertEqual(f.entree.valeur, 47)

        # depilements
        x = f.defiler()
        self.assertEqual(x.valeur, 12)
        f.defiler()
        x = f.defiler()
        self.assertEqual(x.valeur, 47)
        with self.assertRaises(BaseException):  # file vide
            f.defiler()
        with self.assertRaises(BaseException):  # file vide
            f.defiler()


if __name__ == '__main__':
    unittest.main()
