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


""" 
A vous d'écrire les méthodes
est_pleine, est_vide, ajouter, defiler, et les tests qui vont avec (inspirez vous du cas de la pile)
"""
