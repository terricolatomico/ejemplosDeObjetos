class Reloj(object):
    hora = 0
    minuto = 0
    seg = 0
    def dame_hora(self):
        return(str(self.hora) + ":" + str(self.minuto) + ":" + str(self.seg))


reloj = Reloj()
x = reloj.dame_hora()


hora = (int(input("Dime la hora: ")))
minuto = (int(input("Dime los minutos: ")))
seg = (int(input("Dime los segundos: ")))
print(x)