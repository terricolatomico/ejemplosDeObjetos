class Romanos(object):
    entero = 0
    romano = ""
    I: 1
    V: 5
    X: 10
    L: 50
    C: 100
    D: 500
    M: 1000

    def convertir(self, x):
        x = input("Introduce un numero")
        numeros = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }


    def __init__(self, nombre):
        self.nombre = nombre
