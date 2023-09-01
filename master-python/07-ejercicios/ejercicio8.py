"""
Ejercicio 8.
Cuanto es el X por ciento de un numero?   
"""

numero = int(input("Ingrese un numero: "))
porcentaje = int(input(f"Ingrese el porcentaje que quiere sacar del {numero}: "))

resultado = (numero*porcentaje)/100
print(f"El {porcentaje} % de {numero} es: {round(resultado,3)}")