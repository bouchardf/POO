import random
from math import pi

class StringFoo:
    def __init__(self):
        self.set_string = "ce text devrait être en majuscule"
    def set_string(self, string):
        self.set_string = string
    def print_string(self):
        print(self.set_string.upper())


class rectangle():
    def __init__(self, largeur, longueur):
        self.longueur = longueur
        self.largeur = largeur

    def calcul_aire(self):
        return self.largeur * self.longueur

    def afficher_infos(self):
        print("largeur:" self.largeur, "longueur:" self.longueur)



rectangle().print_airerectangle()
    

class cercle():
    def __init__(self, rayon):
        self.rayon = rayon
    def calcul_aire(self):
        return pi * self.rayon ** 2
    def calcul_circonference(self):
        return 2 * pi * self.rayon


class hero():
    def __init__(self, nom):
        self.vie = random.randint(1, 10) + random.randint(1,10)
        self.force = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.nom = nom

    def attaque(self):
        return random.randint(1, 6) + self.force

    def defense(self):
        self.vie -= random.randint(1, 6)

    def est_vivant(self):
        if self.vie < 0:
            return True
        return False
