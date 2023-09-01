"""
Ejercicio 7.
Hacer un programa que muestre todos los impares 
entre dos numeros que diga el usuario.
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 < num2:
    for contador in range(num1, num2+1):
        if contador%2 != 0:
            print(contador, "es Impar")
        else:
            print(contador, "es Par")
else:
    print("El primer numero debe ser menor que el segundo numero")            