
#Operadores condicionales
# Ejemplo 1
print("*************Ejemplo 1**************")
color = "Azul".lower()
#color = input("¿Cual es mi color favorito?: ").lower()

if color == "azul":
    print("En hora buena!!!")
    print("El color es Azul")
else:
    print("Color incorrecto")

"""   
# Operadores de comparacion    
== igual
!= distinto
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

Operadores Logicos
and
or
!
not


"""

# Ejemplo 2
print("\n*************Ejemplo 2**************")

anio = 2020
#anio = int(input("¿En que año estamos?: "))
if anio >= 2021:
    print("Estamos despues de  2021")
else:
    print("Estamos antes de 2021")
    
# Ejemplo 3
print("\n*************Ejemplo 3**************")

nombre = "Pedro"
ciudad = "Buenos Aires"
continente = "America"
edad = 3
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "America":
        print(f"{nombre} no es Americano")
    else:
        print(f"{nombre} es Americano y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")
    
# Ejemplo 4
print("\n*************Ejemplo 4**************")
dia = 3
#dia = int(input("Ingrese el numero del dia de la semana: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")
    
# Ejemplo 5
print("\n*************Ejemplo 5**************")

edad_minima = 18
edad_maxima = 65
edad_real = 23
#edad_real = int(input("Estas en edad de trabajar?: "))

if edad_real >= edad_minima and edad_real <= edad_maxima:
    print("Está en dad de trabajar")
else:
    print("No está en dad de trabajar")

# Ejemplo 6
print("\n*************Ejemplo 6**************")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} SI es un pais de habla Hispana")
else:
    print(f"{pais} NO es un pais de habla Hispana")    

    
# Ejemplo 7
print("\n*************Ejemplo 7**************")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla Hispana")
else:
    print(f"{pais} SI es un pais de habla Hispana") 
    
    
# Ejemplo 8
print("\n*************Ejemplo 8**************")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla Hispana")
else:
    print(f"{pais} SI es un pais de habla Hispana")       