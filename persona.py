class Persona(object):
    edad = ""
    nombre = ""

    def correr(self):
        return("estoy corriendo")
    def saltar(self):
        return("estoy saltando")
    def caminar(self):
        return("estoy caminando")


esteban = Persona()
x = esteban.caminar()
print(x, esteban.saltar())
