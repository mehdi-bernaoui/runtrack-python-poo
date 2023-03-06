class Livre:

	def __init__(self, titre, auteur, pages):
		self.__titre = titre
		self.__auteur = auteur
		self.__pages = pages

	def setInfos(self,nouvelauteur, nouveautitre, nouvellesPages):
		self.__nbPages = nouvellesPages
		self.__titre = nouveautitre
		self.__auteur = nouvelauteur
		if type(self.__nbPages) == int:
			if self.__nbPages > 0:
				self.__pages = self.__nbPages

	def getInfos(self):
		print("Le titre est:", self.__titre)
		print("L'auteur est:", self.__auteur)
		print("Le nombres de pages du livre:", self.__pages)

Livre1 = Livre("Le petit prince", "St Exupérie", 150)
Livre1.getInfos()
Livre1.setInfos("Le portail jaune", "Marcel Pagnol",75)
Livre1.getInfos()