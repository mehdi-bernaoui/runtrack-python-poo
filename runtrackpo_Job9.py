class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def CalculerPrixTTC(self):
        self.TTC = self.prixHT + self.TVA
        print("Le prix TTC du produit ", self.nom, "est de :", self.TTC)
Produit1 = Produit("Lait", 2.30, 0.30)
Produit1.CalculerPrixTTC()
Produit2 = Produit("Oeuf", 2.10, 0.25)
Produit2.CalculerPrixTTC()
Produit3 = Produit("saucisson",8.90, 1.80)
Produit3.CalculerPrixTTC()
Produit4 = Produit("Poulet", 11.50, 2.30)
Produit4.CalculerPrixTTC()