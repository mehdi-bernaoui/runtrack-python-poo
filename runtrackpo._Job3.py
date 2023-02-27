class Operation:

    def __init__(self, nbr1, nbr2):
        self.nombre1 = nbr1
        self.nombre2 = nbr2

    def Addition(self):
        somme = self.nombre1 + self.nombre2
        print(" la somme du Nombre1 et du Nombre2 est :", somme)
    
p = Operation(2, 4)
p.Addition()


