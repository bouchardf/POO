from random import*

class hero():
    def __init__(self, nom):
        self.vie = randint(2, 20)
        self.force = randint(1, 6)
        self.defense = randint(1, 6)
        self.nom = nom

    def attaque(self):
        self.dommage = randint(1, 6) + self.force

    def defense(self):
        self.dommage_defense = self.defense() - self.dommage

    def est_vivant(self):
        if self.vie < 0:
            return "mort"