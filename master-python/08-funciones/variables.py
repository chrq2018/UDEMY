# Variable global

frase = "Hola Pedro"
print(frase)

def holaMundo():
    # variable local
    frase = "Hola Mundo"
    print("Dentro de la funcion")
    print(frase)
    
    global edad
    edad = 30
    print("Dentro: ", edad)
    
holaMundo()
print("Fuera: ", edad)