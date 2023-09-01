nombre = "Luis"

# Funciones generales

print(type(nombre))

# DEtectar el tipado
comprobar = isinstance(nombre, int)
if comprobar:
    print("Es una cadena")
else:
    print("No es una cadena")
    
if not isinstance(nombre, float):
    print("La variable no es un numero con decimal")
    
# Limpiar espacio antes y despues de la cadena
frase = "Hola"
print(frase)
frase = ("     Hola     Mundo    ")
print(frase.strip())   

# Eliminar variables
mes = "enero"
print(mes) 

#del mes
print(mes)

# Comprobar variable vacia

texto = "   hola   "
if len(texto) <= 0:
    print("La variable está vacia")
else:
    print("La variable tiene contenido: ", len(texto))
    
# Encontrar caracteres

frase3 = "La vida es corta"

print(frase3.find("vida"))

# Reemplazar palabras

nueva_frase3 = frase3.replace("vida", "calle")
print(nueva_frase3)

# Mayusculas y minusculas

print(frase3)
print(frase3.lower())
print(frase3.upper())