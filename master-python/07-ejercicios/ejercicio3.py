"""
Ejercicio 3.
Escribir un programa que muestre los 
cuadrados de los 60 primeros numeros 
naturales. Resolverlo con FOR y WHILE
"""
# FOR
for contador in range(61):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
  
print("\n----------------------------------\n")   
    
# WHILE
contador1 = 0
while contador1 <= 60:
    cuadrado1 = contador1*contador1
    print(f"El cuadrado de {contador1} es {cuadrado1}")
    contador1 += 1