class Rectangle:

	def __init__(self, longueur, largeur):
		self.__longueur = longueur
		self.__largeur = largeur

	def setParametres(self):
		self.__longueur = input("Quelle est la nouvelle longueur ?")
		self.__largeur = input("Quelle est la nouvelle largeur ?")

	def getParametres(self):
		print(self.__longueur, self.__largeur)

Rectangle1 = Rectangle(10, 5)
Rectangle1.getParametres()

Rectangle1.setParametres()
Rectangle1.getParametres()