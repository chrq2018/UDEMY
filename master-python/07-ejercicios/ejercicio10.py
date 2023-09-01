"""
Ejercicio 10.
El programa tiene que pedir la nota de 15 alumnos
y mostrar por pantalla cuantos aprobaron y cuantos desaproboron.        
"""
NOTA_MINIMA = 7

contador = 1
acum_aprobados = 0
acum_desaprobados = 0
cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
while contador <= cant_alumnos:
    nota = int(input(f"Ingrese la nota del \"Alumno{contador}\": "))
    if nota >= NOTA_MINIMA:
        acum_aprobados += 1 
    else:
        acum_desaprobados += 1   

    contador += 1
    
print(f"Cantidad de alumnos Aprobados: {acum_aprobados}")
print(f"Cantidad de alumnos Desaprobados: {acum_desaprobados}")