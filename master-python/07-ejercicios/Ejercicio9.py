"""
Ejercicio 9.
Hacer un programa que pida numeros al usuario 
indefinidamente hasta que el usuario ingrese el 111.       
"""
"""
numero = int(input("Ingrese un numero: "))

while numero != 111:
    print(f"Ingreso el {numero}")
    numero = int(input("Ingrese un numero: "))

numero = (input("Acertó!!! "))

"""

# Otra solucion
contador = 1
while contador < 100:
    numero = int(input("Ingrese un numero: "))
    if numero == 111:
        break
    else:
        input(f"Has ingresado el: {numero}")
    
    contador += 1

if numero == 111:
    print("Acerto!!!")        

