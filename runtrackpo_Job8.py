from math import *
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def changerRayon(self):
        self.rayon2 = input("Entrez le Nouveau rayon")
        self.rayon = self.rayon2
        print("Le Rayon a été change voici le nouveau :", self.rayon)
    def afficherInfos(self):
        print("##############################################")
        print("Les informations du cercle actuel sont :")
        print("le rayon du cercle est de :", self.rayon)
        print("La circonférence est de :", Cercle.circonférence(self))
        print("L'aire du cercle est de :", Cercle.aire(self))
        print("Le diametre du cercle est de :", Cercle.diametre(self))
        print("##############################################")
    def circonférence(self):
        self.circonférenceValeur = ((2*pi)*(self.rayon))
        print("La cirfoncérence est de :", self.circonférenceValeur)
    def aire(self):
        self.aireValeur = (pi*(self.rayon)*(self.rayon))
        print("L'aire du cercle est de :", self.aireValeur)
    def diametre(self):
        self.diametreValeur = (2*(self.rayon))
        print("L'aire du Cercle est de :", self.diametreValeur)
    """def menu(self): ############################# C'est un menu qui marche qui me permet de choisir la valeur de l'option
        print("Pour Changer le Rayon entrez 1")
        print("Pour Afficher les Infos entrez 2")
        print("Pour Afficher la Circonférence entrez 3")
        print("Pour Afficher l'aire entrez 4")
        print("Pour Afficher le diametre entrez 5")
        menu2 = 0
        menu = input("Quelle option voulez vous lancer ?")
        menu2 = menu
        if menu2 == "1":
            menucercle.changerRayon()
        elif menu2 == "2":
            menucercle.afficherInfos()
        elif menu2 == "3":
            menucercle.circonférence()
        elif menu2 == "4":
            menucercle.aire()
        elif menu2 == "5":
            print("Vous avez entré 5")
            menucercle.diametre()
        else:
            print("MAL")"""
menucercle1 = Cercle(4)
"""menucercle.menu()"""
menucercle1.afficherInfos()
menucercle1.circonférence()
menucercle1.aire()
menucercle1.diametre()
menucercle2 = Cercle(7)
menucercle2.afficherInfos()
menucercle2.circonférence()
menucercle2.aire()
menucercle2.diametre()