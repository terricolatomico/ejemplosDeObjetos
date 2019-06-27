class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def getnombre(self):
        return self.__nombre

    def getsalario(self):
        return self.__salario

    def setnombre(self):
        return self.__nombre

    def setsalario(self):
        return self.__salario

    def delnombre(self):
        del self.__nombre

    def delsalario(self):
        del self.__salario

empleado1 = Empleado("Francisco", 30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco José")
print(empleado1.getnombre(), ",", empleado1.getsalario())