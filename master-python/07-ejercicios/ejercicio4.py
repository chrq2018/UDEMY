"""
Ejercicio 4.
Pedir dos numeros al usuario y las operaciones 
basicas de una calculadora y mostrar por pantalla.        
"""

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

print("***********CALCULADORA*************")
print(f"La suma es: {num1+num2}")
print(f"La resta es: {num1-num2}")
print(f"La multiplicacion es: {num1*num2}")
print(f"La division es: {round(num1/num2, 2)}")

print("\n--------------------------\n")

print("La suma es: " + str(num1+num2))
print("La resta es: " + str(num1-num2))
print("La multiplicacion es: " + str(num1*num2))
print("La division es: " + str(round(num1/num2, 2)))