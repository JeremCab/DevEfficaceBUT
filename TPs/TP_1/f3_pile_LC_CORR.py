##########################################
# TP dev efficace semaine 1              #
# implementation pile par liste chaînée  #
##########################################



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

class Pile_LC:

    def __init__(self):
        """création d'une pile vide
        """
        self.sommet = None # le haut de la pile

    def est_vide(self):
        """renvoie un booléen indiquant si la pile est vide
        """
        return self.sommet is None

    def empiler(self, x):
        """ajoute x au sommet de la pile

        Args:
            x : élément à empiler

        """
        # on empile en ajoutant un élément en début de liste O(1)
        # attention à l'ordre des mises à jour
        x.suivante = self.sommet  # mise à jour pointeur x
        self.sommet = x           # mettre à jour sommet

    def depiler(self):
        """renvoie et supprime l'élément au sommet de la pile

        Raises:
            Exception: indique que la pile est vide
        """
        if self.est_vide():
            raise Exception("La pile est vide !")
        else:
            x = self.sommet           # enregistre ancien sommet
            self.sommet = x.suivante  # mise à jour du sommet
            return x                  # retourne ancien sommet


class TestPile_LC(unittest.TestCase):

    def test_vide(self):
        """unittests pour pile_vide
        """
        p = Pile_LC()
        self.assertTrue(p.est_vide())

    def test_empiler(self):
        """unittests pour empiler
        """
        p = Pile_LC()
        valeurs = [1, 5, 33, 27, -14]

        for v in valeurs:
            p.empiler(Cellule(v))
            self.assertEqual(p.sommet.valeur, v)

    def test_depiler(self):
        """unittests pour depiler
        """
        p = Pile_LC()
        valeurs = [1, 5, 33, 27, -14]

        for v in valeurs:
            p.empiler(Cellule(v))

        for i in range(len(valeurs)):
            x = p.depiler()
            self.assertEqual(x.valeur, valeurs[len(valeurs)-i-1])

        with self.assertRaises(BaseException):  # pile vide
            p.depiler()
        with self.assertRaises(BaseException):  # pile vide
            p.depiler()

    def test_scenario_complet(self):
        """unittests pour un scenario complet
        """
        # pile vide
        p = Pile_LC()
        self.assertTrue(p.est_vide())

        # empilements
        p.empiler(Cellule(12))
        self.assertEqual(p.sommet.valeur, 12)
        p.empiler(Cellule(3))
        p.empiler(Cellule(47))
        self.assertEqual(p.sommet.valeur, 47)
        self.assertEqual(p.sommet.valeur, 47)

        # depilements
        x = p.depiler()
        self.assertEqual(x.valeur, 47)
        p.depiler()
        x = p.depiler()
        self.assertEqual(x.valeur, 12)
        with self.assertRaises(BaseException):  # pile vide
            p.depiler()
        with self.assertRaises(BaseException):  # pile vide
            p.depiler()


if __name__ == '__main__':
    unittest.main()
