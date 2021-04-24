# Programado por Antonio Gallego. Producciones Tetric Games con motor Surreal

import random

nombre = input("¿Cómo te llamas, piratilla? > ")

print("""
        ,     \    /      ,        
       / \    )\__/(     / \       
      /   \  (_\  /_)   /   \      
 ____/_____\__\@  @/___/_____\____ 
|             |\../|              |
|              \VV/               |""")

# Esta chorrada es lo que más me ha costado
titulo = nombre + "'s Game"
p=int((34-len(titulo))/2) # padding
if len(titulo)%2==1:
    q = p
else:
    q = p-1
print("|"+" "*p+titulo+" "*q+"|")

print("""|_________________________________|
 |    /\ /      \\\\       \ /\    | 
 |  /   V        ))       V   \  | 
 |/     `       //        '     \| 
 `              V                '
""")

input("Y ahora, {}, dale al ENTER si estás listo".format(nombre)) #pausa

print("\nPero antes de continuar, {}, un consejo\n"
      "Este vídeo está patrocinado por GVGMall\n"
      "Blah Blah Blah Blah Blah Blah\n"
      "OK, al lío\n".format(nombre))

opcion1 = input("Vas por el campo cuando un OVNI gigante te abduce\n"
               "Te despiertas en la nave nodriza de los marcianos\n"
               "Hay unos extraterrestres con una jeringa chunga a tu lado\n"
               "En una repisita ves un objeto negro brillante\n"
               "(A) Tratas de despistarles para coger el objeto (B) Te pones a discutir con ellos  > ")

if opcion1 == "A":
    print("\n- ¡Hostiás! ¿Qué es eso? - dices apuntando por la ventanilla de la nave\n"
          "Mientras miran los marcianos aprovechas para meterte el objeto de la repisa en el bolsillo...\n")

tienes_el_satisfier_de_los_marcianos = (opcion1 == "A")

opcion2 = input("Los marcianos se mosquean y se van a por tí\n"
                "(A) Huyes hacia el teletransportador (B) Intentas ponerte al volante de la nave > ")
if opcion2=="A":
    print("En el teletransportador se cuela una mosca justo a la que entras\n"
          "si has visto la película sabes que la cosa acaba mal :-(\n")
elif opcion2 == "B":
    opcion3 = input(("Saltas raudo a los mandos de la nave\n"
            "Hay un botón gordo rojo que pone SCRAM en marciano\n"
            "(A) Le das al botón (B) Le das muy fuerte al botón > "))
    if opcion3 == "A":
        print("¡Bravo {}, has saltado de la nave!\n".format(nombre))
        print("Vuelves a la Tierra. Estás a salvo...")
        if tienes_el_satisfier_de_los_marcianos:
            print("¡Además robaste el satisfier de los Marcianos!\n"
                  "¡¡Tienes tecnología extraterrestre!!\n"
                  "¡¡¡Todo el mundo te cree, eres un héroe mundial!!! :-)\n")
        else:
            print("...pero nadie te cree. Todo el mundo piensa que estás como una chota.\n"
                  " Al menos te salvaste :-P")
    elif opcion3 =="B":
        print("¡Joder, {}, has roto el botón! Ahora los marcianos van a acabar contigo fijo :-(".format(nombre))
        premio = random.randint(1,6)
        dado = int(input("Rápido, tira un dado > "))
        if dado != premio:
            print("Saltaste al hiperespacio, apareces junto a Low Spec Gamer\n"
                  "Te dedicas el resto de tu vida a rular la demo del Assasins en laptops cutres :-/")
        else:
            print("Los marcianos están hasta los huevos de tí y te mandan a un zoo en Ceres :-(")
    else:
        print("Te has hecho la picha un lío y te han terminado tirando por el retrete de la nave :-(")
else:
    print("Los marcianos te venden a Jabba the Hutt, y acabas en una plancha de carbono :-(")
