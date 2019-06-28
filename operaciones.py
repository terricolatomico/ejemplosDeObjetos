class operaciones(object):
    def __init__(self, num1, num2): #inicializando la clase
        self.num1 = num1 #este numero 1 es igual al numero 1 que viene
        self.num2 = num2 #este numero 2 es igual al numero 2 k viene

    def suma(self):
        return self.num1 + self.num2  # las variables dentro de las clases

    def resta(self):
        return self.num1 - self.num2





#principal
objeto1 = operaciones(8, 52) # a la hora de crear el objeto es cuando se le pasan los valores
print(objeto1.suma())
print(objeto1.resta())
