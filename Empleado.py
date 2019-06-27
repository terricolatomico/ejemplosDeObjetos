class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def getnombre(self):
        return self.__nombre

    def getsalario(self):
        return self.__salario

    def setnombre(self, nombre):
        return self.__nombre = nombre

    def setsalario(self, salario):
        return self.__salario = salario

    def delnombre(self):
        del self.__nombre

    def delsalario(self):
        del self.__salario

