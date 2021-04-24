from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
LON_BARRA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Turnos

    # Turno Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0

    #print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))
    barra_pikachu = int((LON_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
    barra_squirtle = int((LON_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
    #print("Pikachu  [" + "#" * barra_pikachu  + " " * (10-barra_pikachu)  + "] {}".format(vida_pikachu))
    #print("Squirtle [" + "#" * barra_squirtle + " " * (10-barra_squirtle) + "] {}".format(vida_squirtle))
    print("Pikachu:  [{}{}] ({}/{})".format("#" * barra_pikachu,  " " * (LON_BARRA - barra_pikachu),  vida_pikachu,  VIDA_INICIAL_PIKACHU))
    print("Squirtle: [{}{}] ({}/{})".format("#" * barra_squirtle, " " * (LON_BARRA - barra_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("ENTER para continuar")
    os.system("cls")

    if vida_pikachu < 0 or vida_squirtle < 0:
        break

    # Turno Squirtle
    print("Turno de Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ['P', 'A', 'B', 'N']:
        ataque_squirtle = input("¿Qué ataque quieres realizar? [P]lacaje, Pistola [A]gua, [B]urbuja [N]ada> ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no ataca en este turno")

    if vida_pikachu < 0:
        vida_pikachu = 0

    #print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))
    barra_pikachu = int((LON_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
    barra_squirtle = int((LON_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
    #print("Pikachu  [" + "#" * barra_pikachu  + " " * (10-barra_pikachu)  + "] {}".format(vida_pikachu))
    #print("Squirtle [" + "#" * barra_squirtle + " " * (10-barra_squirtle) + "] {}".format(vida_squirtle))
    print("Pikachu:  [{}{}] ({}/{})".format("#" * barra_pikachu,  " " * (LON_BARRA - barra_pikachu),  vida_pikachu,  VIDA_INICIAL_PIKACHU))
    print("Squirtle: [{}{}] ({}/{})".format("#" * barra_squirtle, " " * (LON_BARRA - barra_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("ENTER para continuar")
    os.system("cls")

if vida_pikachu > vida_squirtle:
    print("Gana Pikachu")
else:
    print("Gana Squirtle")