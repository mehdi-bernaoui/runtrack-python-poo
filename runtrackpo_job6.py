class Animal:

    def __init__(self):
        self.age = 0
        self.age2 = input("Entrez l'age de l'animal :")
        self.age = self.age2
        print("L'animal a :",self.age)

    def Vieillir(self):
        self.age = int(self.age) + 1
        print("# Age de l'animal apres appel de la methode vieillir :")
        print("L'animal a :",self.age)

    def nommer(self):
        self.prenom = ""
        self.prenom2 = input("Entrez le prénom de l'animal :")
        self.prenom = self.prenom2
        print("L'animal se nomme", self.prenom)

Animal1 = Animal()
Animal1.Vieillir()
Animal1.nommer()
        
        