"""
Ejercicio 2.
Escribe un script que nos muestre por pantalla
todos los numeros pares del 1 al 120
"""

for contador in range(0, 121, 2):
    print(f"{contador}")
    
for contador1 in range(1,121):
    if contador1%2 == 0:
        print(f"{contador1} es par" ) 