from math import pi

class circulo(object):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio**2 * pi

    def perimetro(self):
        return 2 * pi * self.radio





