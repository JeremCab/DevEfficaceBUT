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
        pass

    def ajouter_debut(self, x):
        """ Ajoute x en tête de la liste L """
        pass


    def ajouter_fin(self, x):
        """ Ajoute le x en queue de la liste """
        pass

    def supprimer_debut(self):
        """ Supprime le 1er élément de la liste et le renvoie """
        pass

    def supprimer_fin(self):
        """ Supprime le dernier maillon de la liste et le renvoie """
        pass
    
    def rechercher(self, valeur):
        """ Recherche valeur dans la liste et renvoie l'élément associé """
        pass

    def afficher_liste(self):
        """ Affiche les éléments de la liste """
        pass



l = LC()

print("\ntest vide")
print(l.est_vide())

print("\ntest ajouter debut")
l.afficher_liste()
x = Cellule(3)
l.ajouter_debut(x)
l.afficher_liste()
# x = Cellule(12)
# l.ajouter_debut(x)
# l.afficher_liste()
# x = Cellule(-5)
# l.ajouter_debut(x)
# l.afficher_liste()

# print("\ntest ajouter fin")
# # l.afficher_liste()
# x = Cellule(100)
# l.ajouter_fin(x)
# l.afficher_liste()
# x = Cellule(200)
# l.ajouter_fin(x)
# l.afficher_liste()
# x = Cellule(300)
# l.ajouter_fin(x)
# l.afficher_liste()

# print("\ntest supprimer debut")
# # l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# l.supprimer_debut()
# l.afficher_liste()
# # #
# # l.supprimer_debut()
# # l.afficher_liste()
# # l.supprimer_debut()
# # l.afficher_liste()
# # l.supprimer_debut()
# # l.afficher_liste()
# # l.supprimer_debut()
# # l.afficher_liste()
# # l.supprimer_debut()
# # l.afficher_liste()
# # l.supprimer_debut()
# # l.afficher_liste()

# print("\ntest supprimer fin")
# # l.afficher_liste()
# l.supprimer_fin()
# l.afficher_liste()
# l.supprimer_fin()
# l.afficher_liste()
# l.supprimer_fin()
# l.afficher_liste()
# # #
# # l.supprimer_fin()
# # l.afficher_liste()

# print("\ntest rechercher")
# # l.afficher_liste()
# x = Cellule(3)
# l.ajouter_debut(x)
# x = Cellule(12)
# l.ajouter_debut(x)
# x = Cellule(-5)
# l.ajouter_debut(x)
# x = Cellule(47)
# l.ajouter_debut(x)
# x = Cellule(-55)
# l.ajouter_debut(x)

# x = l.rechercher(47)
# print(x.valeur)
# l.afficher_liste()
# x = l.rechercher(12)
# print(x.valeur)
# l.afficher_liste()
# x = l.rechercher(-55)
# print(x.valeur)
# l.afficher_liste()
# x = l.rechercher(3)
# print(x.valeur)
# l.afficher_liste()
