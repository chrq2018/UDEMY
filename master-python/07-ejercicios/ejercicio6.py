"""
Ejercico 6.
Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.
"""

print("\n##### Tablas de multiplicar del 1 al 10 #####\n")
for cabecera in range(1,11):
    print("************************************")
    print(f"**** Tabla de multiplicar del {cabecera} ****")
    print("************************************")
    for contador1 in range(1,11):
        print(f"{cabecera} x {contador1} = {cabecera*contador1}")
    
    print("\n")