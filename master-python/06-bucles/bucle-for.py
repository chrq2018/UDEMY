"""
# FOR

for variable in elemento_iterable(lista, rango, tubla, etc)
    BLOQUE DE INSTRUCCIONES    
    
"""

contador = 0
resultado = 0
for contador in range(8, 15):
    print(f"voy por el {contador}") 
    resultado += contador
    
print(f"la suma es {resultado}")

# Ejelmplo tabla des de multiplicar
print("\n***************** EJEMPLO *******************")

numero_usuario = int(input("¿De que numero desea ver la tabla?: "))
print(f"\n************ Tabla de multiplicar del {numero_usuario} ******************")
if numero_usuario < 1:
        numero_usuario = 1
        
for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("No se puede multiplicar un numero prohibido")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada!!")
