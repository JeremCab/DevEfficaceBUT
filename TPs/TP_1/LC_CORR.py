##########################################
# TP dev efficace semaine 1              #
# implementation pile par liste chaînée  #
##########################################


import unittest


class Cellule:
    def __init__(self, valeur, suivant=None):
        """création d'une cellule

        Args:
            valeur (quelconque): la valeur à stocker dans la cellule
            suivante (Cellule): la cellule suivante de la liste chaînée
        """
        self.valeur = valeur
        self.suiv = suivant


class LC:

    def __init__(self):
        """création d'une liste chaînée
        """
        self.tete = None  # premier élément de la liste

    def est_vide(self):
        """renvoie un booléen indiquant si la liste est vide
        """
        return self.tete is None

    def ajouter_debut(self, x):
        """ Ajoute x en tête de la liste L """
        x.suiv = self.tete
        self.tete = x

    def ajouter_fin(self, x):
        """ Ajoute le x en queue de la liste """
        m = self.tete
        while m.suiv is not None:
            m = m.suiv
        m.suiv = x

    def supprimer_debut(self):
        """ Supprime le 1er élément de la liste et le renvoie """
        if self.est_vide():
            raise Exception("La pile est vide !")
        t = self.tete
        self.tete = t.suiv
        return t

    def supprimer_fin(self):
        """ Supprime le dernier maillon de la liste et le renvoie """
        if self.est_vide():           # pile vide
            raise Exception("La pile est vide !")
        elif self.tete.suiv is None:  # 1 seule element
            e = self.tete
            self.tete = None
            return e
        else:                         # au moins 2 elements
            e = self.tete
            e_courant = self.tete
            while e.suiv is not None:
                e_courant = e
                e = e.suiv
            e_courant.suiv = None
            return e
    
    def rechercher(self, valeur):
        """ Recherche valeur dans la liste et renvoie l'élément associé """
        if self.est_vide():
            raise Exception("La pile est vide !")
        else:
            e = self.tete
            while e is not None:
                if e.valeur == valeur:
                    print("element trouvé")
                    return e
                else:
                    e = e.suiv

    def afficher_liste(self):
        """ Affiche les éléments de la liste """
        if self.est_vide():
            print("liste vide")
        else:
            e = self.tete
            while e.suiv is not None:
                print(e.valeur, end=" ")
                e = e.suiv
            print(e.valeur, end="\n")



l = LC()

print("\ntest vide")
print(l.est_vide())

print("\ntest ajouter debut")
# l.afficher_liste()
x = Cellule(3)
l.ajouter_debut(x)
l.afficher_liste()
x = Cellule(12)
l.ajouter_debut(x)
l.afficher_liste()
x = Cellule(-5)
l.ajouter_debut(x)
l.afficher_liste()

print("\ntest ajouter fin")
# l.afficher_liste()
x = Cellule(100)
l.ajouter_fin(x)
l.afficher_liste()
x = Cellule(200)
l.ajouter_fin(x)
l.afficher_liste()
x = Cellule(300)
l.ajouter_fin(x)
l.afficher_liste()

print("\ntest supprimer debut")
# l.afficher_liste()
l.supprimer_debut()
l.afficher_liste()
l.supprimer_debut()
l.afficher_liste()
l.supprimer_debut()
l.afficher_liste()
# #
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()

print("\ntest supprimer fin")
# l.afficher_liste()
l.supprimer_fin()
l.afficher_liste()
l.supprimer_fin()
l.afficher_liste()
# l.supprimer_fin()
# l.afficher_liste()
# #
# l.supprimer_fin()
# l.afficher_liste()

print("\ntest rechercher")
# l.afficher_liste()
x = Cellule(3)
l.ajouter_debut(x)
x = Cellule(12)
l.ajouter_debut(x)
x = Cellule(-5)
l.ajouter_debut(x)
x = Cellule(47)
l.ajouter_debut(x)
x = Cellule(-55)
l.ajouter_debut(x)

x = l.rechercher(47)
print(x.valeur)
l.afficher_liste()
x = l.rechercher(12)
print(x.valeur)
l.afficher_liste()
x = l.rechercher(-55)
print(x.valeur)
l.afficher_liste()
x = l.rechercher(3)
print(x.valeur)
l.afficher_liste()
