from objetos1 import *
from factura import *
from Empleado import *

# et = Objeto()
# print(et.color)
# print(et.tamanio)
# print(et.aspecto)
# et.color = "rosa"
# print(et.color)

objeto = Objeto( )
print(Objeto.color)
Objeto.tamanio = "pequenio"
x = NuevoObjeto()
print(x.pie.color)
v = x.pie.amputar()
print(v)

# de factura
compra1 = Factura(12, 110)
print(compra1.unidad)
print(compra1.precio)
print(compra1.a_pagar(), "Euros")
# print(compra1._Factura.__tasa) No se puedfe acceder a privados


#de empleado
empleado1 = Empleado("Francisco", 30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco José")
print(empleado1.getnombre(), ",", empleado1.getsalario())



