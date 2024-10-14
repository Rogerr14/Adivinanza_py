

import random


def juego_adivinanza():
    #generar un numero de 1 al 100
    numero_secreto = random.randint(1,100)
    intentos= 0
    adivinado = False
    
    print("bienvenido al juego de adivinanza")
    print("Adivina un numero del 1 al 100")

    while not adivinado:
      numero = input("ingrese un numero: ")
      if numero.isdigit():
         numero = int(numero)
         intentos +=1
         if numero > numero_secreto:
            print("el numero ingresado es mayor al numero secreto")
         elif numero < numero_secreto:
            print("el numero ingresado es menor al numero secreto")
         elif numero == numero_secreto:
            print(f"Acertaste el numero es {numero_secreto}")
            print(f"N° de intentos {intentos}")
            adivinado = True


juego_adivinanza()
         

         
         


