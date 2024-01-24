#Importamos la librería necesaria
import random

#Definimos los rangos de juegos que habrá
rangopp = {"25": 5 ,"50": 5, "100": 7, "500": 10}

print("RANGOS DISPONIBLES:")
print("25. 5 Oportunidades")
print("50. 5 Oportunidades")
print("100. 7 Oportunidades")
print("500. 10 Oportunidades")

#Preguntamos en que rango vamos a jugar
oport = input("De cero a que rango encontraré tu número? Esto definirá a su vez las oportunidades que tendré: ")

#Creamos el contador de oportunidades
cont = 1

#Creamos el numero mas alto conocido y mas bajo
above = int(oport)
below = 0


while cont <= rangopp[str(oport)]:

    #DEBUGGINGGGGGGGG
    #print(f"Above = {above}")
    #print(f"Below = {below}")

    #Creamosun numero aleatorio en rango y preguntamos si es ese
    res = random.randrange(below,above)
    acc = input(f"Estabas pensando en el numero {res}? y/n: ")

    #Si lo es gana la maquina
    if acc == "y":
        print("¡Correcto! Soy el mejor.")
        break
    else:
        #Si no lo es modificamos el rango con el que estabamos trabajando
        aborbe = input("Es mayor o menor que el número que te he dado? (higher or lower) h/l: ")
        if aborbe == "h":
            #print("Lo tendre como tope por abajo.")
            below = res+1
        else:
            above = res-1
            #print("Lo tendre como tope por arriba.")
        
    #Añadimos un intento al contador
    cont += 1

if cont > rangopp[str(oport)]:
    print("Has conseguido ganar a una maquina.")
