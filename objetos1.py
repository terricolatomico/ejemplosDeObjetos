class Antena():
    color = ""
    longitud = ""
class Pelo():
    color = ""
    longitud = ""
class Ojo():
    color = ""
    longitud = ""

class Objeto(object):
    color = "verde"
    longitud = "mediana"
    tamanio = "grande"
    aspecto = "feo"
    antenas = Antena()  #propiedad compuesta por el objeto Antena()
    ojos = Ojo()        #propiedad compuesta por el objeto Ojo()
    pelos = Pelo()      #propiedad compuesta por el objeto Pelo()


    def flotar(self):
        return("flotar")


class Dedo(object):
    longitud = ""
    forma = ""
    color = ""

class Pie(object):
    forma = ""
    color = ""
    dedos = Dedo()

    def amputar(self):
        return ("se corto el pie")


class NuevoObjeto(object):
    pie = Pie()

    def saltar(self):
        return("saltar")