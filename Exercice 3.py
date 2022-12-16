from math import pi

class cercle():
    def __init__(self):
        self.rayon = 5
        self.circonferance = 2 * pi * self.rayon
        self.aire = pi * self.rayon ** 2

    def set_circonferance(self, circonferance):
        self.circonferance = circonferance

    def set_aire(self, aire):
        self.aire = aire

    def print_circonferance(self):
        print(self.circonferance)

    def print_aire(self):
        print(self.aire)

cercle().print_circonferance()
cercle().print_aire()