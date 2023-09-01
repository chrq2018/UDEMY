"""
#BUCLE WHILE    
    
    
"""
contador = 1
while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador += 1
    
print("\n--------------------------------------------------")

contador1 = 1
muestrame = str(0)
while contador1 <= 100:
    muestrame = muestrame + ", " + str(contador1)
    contador1 += 1
    
print(muestrame)

# Ejelmplo tabla des de multiplicar
print("\n***************** EJEMPLO *******************")

numero_usuario = int(input("¿De que numero desea ver la tabla?: "))
print(f"\n************ Tabla de multiplicar del {numero_usuario} ******************")

cont2 = 1        
while cont2 <= 10:
    print(f"{numero_usuario} x {cont2} = {numero_usuario*cont2}")
    cont2 += 1
else:
    print("Tabla terminada!!")