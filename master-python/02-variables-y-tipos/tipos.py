"""
None
int
str
bool
float
list
tuple
dict
range
bytes
set
    
"""

nada = None
cadena = "Hola"
entero = 3
flotante = 4.3
booleano = True
lista = [3,6,"hola", 4.7]
tuplaNoCambia = ("juan", 45, "perez", 6.9)
diccionario = {1:"lunes", 2:"martes", 3:"viernes"}
rango = range(9)
dato_byte = b"probando"

print(type(nada))
print(type(lista))
print(type(diccionario))
print(type(rango))
print(rango)
print(dato_byte)
print(type(dato_byte))

#convertir datos

texto = "Hola Juan"
numero4 = 456

print(texto + " " + str(numero4))