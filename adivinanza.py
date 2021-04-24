import random

numero = random.randint(1,10)

eleccion = int(input("Dime un numero del 1 al 10 > "))

if eleccion == numero:
    print("¡Ganaste!")

print("Era el {}".format(numero))