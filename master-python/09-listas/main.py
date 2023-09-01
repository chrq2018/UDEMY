"""
LISTAS (arrays)

"""
"""
# Definir lista
peliculas = ["Batman", "Hulk", "Superman", "Thor"]
cantantes = list(("Madona", "Sting", "Jairo", "Bruce"))
anios = list(range(2020, 2050))
variada = ["Juan", 2023, True, "otro text", 34.7]

print(peliculas)
print(cantantes)
print(anios)
print(variada)

# Indices
peliculas[1] = "Gran Torino"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3]) # no muestra el elemto 3
print(peliculas[1:])
print(peliculas[0:])

# Añadir elemntos a una lista
cantantes.append("Chico Novarro")
print(cantantes)

"""
"""
# Recorrer lista
peliculas = ["Batman", "Hulk", "Superman", "Thor"]

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = str(input("ingrese pelicula: "))
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


print("\n*********LISTADO DE PELICULAS************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")

"""


# Listas multidimensionales
print("*************LISTADO DE CONTACTOS*****************") 
contactos =[
    [
        "Luis",
        "luis@gmail.com",
        22222222
    ],
    [
        "Juan",
        "juan@gmail.com",
        33333333
    ],
    [
        "Pedro",
        "pedro@gmail.com",
        55555555
    ]
]
print("--------------------------")
print(contactos)
print(contactos[2][1])
print()
print("Mostrar los mail")
for contacto in contactos:
    print(contacto[1])
print("--------------------------")
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("nombre: " + elemento)
        elif contacto.index(elemento) == 1:
            print("mail: " + elemento)
        else:
            print("telefono: ", elemento)
    print()    