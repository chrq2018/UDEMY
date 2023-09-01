# FUNCIONES

# Ejemplo 1
print("********** EJEMPLO 1 *********")

# Definir funcion
def muestraNombres():
    print("Pedro")
    print("Juana")
    print("Luis")
    print("Agustina")
    print("Ignacio")
    print("\n")
    
# Invocar funcion    
muestraNombres()

# Ejemplo 2: Parametros
print("\n********** EJEMPLO 2 *********")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")
        
#nombre = str(input("Ingresa tu nombre: "))  
#edad = int(input("Ingresa tu edad: ")) 
nombre = "juan"
edad = 34
mostrarTuNombre(nombre, edad)

# Ejemplo 3
print("\n********** EJEMPLO 3 *********")

def tabla(numero):
    print(f"Tabla de multiplicar del: {numero}")
    for i in range(1, 11):
        resultado = numero*i
        print(f"{numero} x {i} = {int(resultado)}")
    print("\n")    
   
numero = 5 
#numero = int(input("Ingrese el numero: "))
tabla(numero)

# Ejemplo 3.1
print("//////////////////////////////////////")
print("\n********** EJEMPLO 3.1 *********")

for i in range(1, 11):
    tabla(i)
    
# Ejemplo 4: Parametros opcionales
print("\n********** EJEMPLO 4 *********")

def getEmpleado(nombre, dni = None):
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

nombre_empleado = "Pedro"
getEmpleado(nombre_empleado)
print("\n")
dni = 2345612
getEmpleado(nombre_empleado, dni)
print("\n")

# Ejemplo 5: Return
print("\n********** EJEMPLO 5 *********")

def saludame(nombre):
    return f"Hola {nombre}"

nombre = "Pedro"
print(saludame(nombre))

print("\n")
# Ejemplo 6
print("\n********** EJEMPLO 6 *********")

def calculadora(num1, num2, basicas = False):
    suma = num1+num2
    resta = num1-num2
    multi = num1*num2
    division = round(num1 / num2, 2)
    
    cadena = ""
    if basicas == False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)
        print("\n")
        
    return cadena
    
print(calculadora(4, 8, False))


# Ejemplo 7
print("\n********** EJEMPLO 7 *********")

def getNombre(nombre):
    texto = f"En nombre es: {nombre}"
    return texto


def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

unNombre = "Pedro"
unApellido = "Boria"

print(devuelveTodo(unNombre, unApellido))


# Ejemplo 8: funcion Lambda
print("\n********** EJEMPLO 8 *********")

dime_el_anio = lambda anio: f"El año es {anio}"
anio = 2055
print(dime_el_anio(anio))
