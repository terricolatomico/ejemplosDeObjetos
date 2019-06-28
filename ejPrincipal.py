from rectangulo import *
from fraseReves import *
from circulo import *



#clase rectangulo
base = int(input("Dime la base: "))
altura = int(input("Dime la altura: "))
poligono1 = rectangulo(base, altura)
print("el area del rectángulos con base:", poligono1.base, "y altura:", poligono1.altura, "es:", poligono1.area())

#clase circulo
radio = int(input("Dime el rádio del círculo: "))
poligono2 = circulo(radio)
print("el área del circulo con radio:", poligono2.radio, "es:", poligono2.area(), "y el perimetro es:", poligono2.perimetro() )

#clase frasereves
frase = str(input("Dime una frase: "))
objetoFrase = FraseReves(frase)
print(objetoFrase.invertir())