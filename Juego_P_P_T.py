#Importar libreria
import random
#Opciones
op = ("Piedra","Papel","Tijera")
#Estructura while
while True:
    #Entradas
    usuario = input("Digite la opción Pierdra, Papel o Tijera:  ")
    cpu = random.choice(op)
    #Imprimir informacion
    print(f"La op que digito el usuario es: {usuario}")
    print(f"La op CPU es: {cpu}")
    #Proceso
    if usuario == "Piedra" and cpu == "Piedra":
        print("Empate!!!")
    elif usuario == "Tijera" and cpu == "Tijera":
        print("Empate!!!")
    elif usuario == "Papel" and cpu == "Papel":
        print("Empate!!!")
    elif usuario == "Piedra" and cpu == "Papel":
        print("Gana cpu!!!")
    elif usuario == "Piedra" and cpu == "Tijera":
        print("Gana usuario!!!")
    elif usuario == "Papel" and cpu == "Piedra":
        print("Gana usuario!!!")
    elif usuario == "Papel" and cpu == "Tijera":
        print("Gana cpu!!!")
    elif usuario == "Tijera" and cpu == "Piedra":
        print("Gana cpu!!!")
    elif usuario == "Tijera" and cpu == "Papel":
        print("Gana usuario!!!")
    else:
        print("Error!!!")
