class Personnage:
    def __init__(self, x, y):
        self.coordonnéeX = x
        self.coordonnéeY = y
    def AffichagePlateau(self):
        M = [["x1y1","x2y1","x3y1"], ["x1y2","x2y2","x3y2"], ["x1y3","x2y3","x3y3"]]
    def gauche(self):
        self.coordonnéeX = int(self.coordonnéeX) -1
    def droite(self):
        self.coordonnéeX = int(self.coordonnéeX) +1
    def bas(self):
        self.coordonnéeY = int(self.coordonnéeY) -1
    def haut(self):
        self.coordonnéeY = int(self.coordonnéeY) +1
    def position(self):
        print("les coordonnées sont X et Y :", self.coordonnéeX, "X", self.coordonnéeY, "Y")

jeu1 = Personnage(5, 2)
jeu1.position()
