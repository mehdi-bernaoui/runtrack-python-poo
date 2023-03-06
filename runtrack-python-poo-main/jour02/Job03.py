class Livre:

	def __init__(self, titre, auteur, pages):
		self.__titre = titre
		self.__auteur = auteur
		self.__pages = pages
		self.__disponible = True

	def setInfos(self, nouvellesPages):
		self.__nbPages = nouvellesPages
		if type(self.__nbPages) == int:
			if self.__nbPages > 0:
				self.__pages = self.__nbPages

	def getInfos(self):
		print("Le titre est:", self.__titre)
		print("L'auteur est:", self.__auteur)
		print("Le nombres de pages du livre:", self.__pages)

	def verification(self):
		if self.__disponible == True:
			return True
		else:
			return False

	def emprunter(self):
		dispo = self.verification()
		if dispo == True:
			self.__disponible = False
			print("Vous empruntez le livre")
			return True
		else:
			print("Vous ne pouvez pas empruntez le livre")
			return False

	def rendre(self):
		dispo = self.verification()
		if dispo == False:
			self.__disponible = True
			print("Vous rendez le livre")
		else:
			print("Vous n'avez pas empruntez le livre")

Livre1 = Livre("Le petit prince", "St Exupérie", 150)
Livre1.verification()
Livre1.emprunter()
Livre1.rendre()