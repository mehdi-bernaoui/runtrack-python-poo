class Point:
    def __init__(self, x, y):
        self.coordonnéeX = x
        self.coordonnéeY = y
    def afficherLesPoints(self):
        print("les Coordonnées X et Y sont :", self.coordonnéeX, self.coordonnéeY)
    def afficherX(self):
        print("la coordonnée X =", self.coordonnéeX)
    def afficherY(self):
        print("la coordonnée Y =", self.coordonnéeY)
    def changerX(self, x2):
        self.coordonnéeX = x2
        print("les coordonnées ont été changée et sont maintenant en X :", self.coordonnéeX)
    def changerY(self, y2):
        self.coordonnéeY = y2
        print("les coordonnées ont été changée et sont maintenant en Y :", self.coordonnéeY)

point = Point(3, 5)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(4)
point.changerY(9)