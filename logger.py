import random

intentos = 0
aciertos = 0

def adivinador(num,oport,rango):
    #Creamos el contador de oportunidades
    cont = 1

    #Creamos el numero mas alto conocido y mas bajo
    above = rango
    below = 0


    while cont < oport:
        
        #Si el tope superior e inferior es ese numero
        if above == below:
            return True

        #Creamos un numero aleatorio en rango y preguntamos si es ese
        res = random.randrange(below,above)

        if res == num:
            return True
        else:
            if res < num:
                #print("Lo tendre como tope por abajo.")
                below = res
            else:
                #print("Lo tendre como tope por arriba.")
                above = res
              
            #Añadimos un intento al contador
            cont += 1

    #si hemos superado las oportunidades devolvemos false
    if cont >= oport:
        return False


#Pongamoslo a prueba
while intentos < 1000000:
    #Si da true la funcion significa que h acertado
    if adivinador(random.randrange(0,1000000), 1, 1000000) == True:
        aciertos += 1
    #Si o si sumamos un intento
    intentos += 1

print(f"He hecho {intentos} y he acertado {aciertos}.")