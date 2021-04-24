# Snakemon, by Antonio Gallego
# mailto: amturing@gmail.com
# ASCII Art Text thanks to http://patorjk.com/software/taag
# ASCII Art borrowed from https://www.asciiart.eu/video-games/pokemon

import random
import readchar
import os

banner = """\
                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                       /^\/^\\
                     _|_O| O |      IN EASY MODE WALLS STOP YOU
            \/     /~     \_/  \\     IN HARD MODE WALLS KILL YOU
             \____|__________/  \\
                    \_______      \\
                            `\     \                 \\
                              |     |                  \\
                             /      /      WASD          \\
                            /     /       to move         \\\\
                          /      /       0 to quit         \ \\
                         /     /                            \  \\
                       /     /             _----_            \   \\
                      /     /           _-~      ~-_         |   |
                     (      (        _-~    _--_    ~-_     _/   |
                      \      ~-____-~    _-~    ~-_    ~-_-~    /
                        ~-_           _-~          ~-_       _-~
  BY ANTONIO               ~--______-~                ~-___-~

███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║
███████╗██╔██╗ ██║███████║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
███████║██║ ╚████║██║  ██║██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\
"""

banner_battle_won = """
██████╗  █████╗ ████████╗████████╗██╗     ███████╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██║    ██║██╔═══██╗████╗  ██║██║
██████╔╝███████║   ██║      ██║   ██║     █████╗      ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝      ██║███╗██║██║   ██║██║╚██╗██║╚═╝
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝
"""

banner_battle_lost = """
 ▄▄▄▄    ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████     ██▓     ▒█████    ██████ ▄▄▄█████▓ ▐██▌ 
▓█████▄ ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀    ▓██▒    ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ▐██▌ 
▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███      ▒██░    ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░ ▐██▌ 
▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄    ▒██░    ▒██   ██░  ▒   ██▒░ ▓██▓ ░  ▓██▒ 
░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒   ░██████▒░ ████▓▒░▒██████▒▒  ▒██▒ ░  ▒▄▄  
░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░    ░▀▀▒ 
▒░▒   ░   ▒   ▒▒ ░   ░        ░    ░ ░ ▒  ░ ░ ░  ░   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ░  ░ 
 ░    ░   ░   ▒    ░        ░        ░ ░      ░        ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░          ░ 
 ░            ░  ░                     ░  ░   ░  ░       ░  ░    ░ ░        ░            ░    
      ░                                                                                       
"""

banner_win = """
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝

                            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗                                  
                            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║                                  
                             ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║                                  
                              ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝                                  
                               ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗                                  
                               ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝     
"""

banner_lost = """
                               ▒█████   ██░ ██     ███▄    █  ▒█████   ▐██▌                 
                              ▒██▒  ██▒▓██░ ██▒    ██ ▀█   █ ▒██▒  ██▒ ▐██▌                 
                              ▒██░  ██▒▒██▀▀██░   ▓██  ▀█ ██▒▒██░  ██▒ ▐██▌                 
                              ▒██   ██░░▓█ ░██    ▓██▒  ▐▌██▒▒██   ██░ ▓██▒                 
                              ░ ████▓▒░░▓█▒░██▓   ▒██░   ▓██░░ ████▓▒░ ▒▄▄                  
                              ░ ▒░▒░▒░  ▒ ░░▒░▒   ░ ▒░   ▒ ▒ ░ ▒░▒░▒░  ░▀▀▒                 
                                ░ ▒ ▒░  ▒ ░▒░ ░   ░ ░░   ░ ▒░  ░ ▒ ▒░  ░  ░                 
                              ░ ░ ░ ▒   ░  ░░ ░      ░   ░ ░ ░ ░ ░ ▒      ░                 
                                  ░ ░   ░  ░  ░            ░     ░ ░   ░                    

                     ▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▄▄▄█████▓ ▐██▌ 
                      ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ▐██▌ 
                       ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░ ▐██▌ 
                       ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒░ ▓██▓ ░  ▓██▒ 
                       ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒  ▒██▒ ░  ▒▄▄  
                        ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░    ░▀▀▒ 
                      ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ░  ░ 
                      ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░          ░ 
                      ░ ░         ░ ░     ░            ░  ░    ░ ░        ░            ░    
                      ░ ░                                                                   

"""
def battle():
    VIDA_INICIAL_PIKACHU = 80
    VIDA_INICIAL_SQUIRTLE = 90
    LON_BARRA = 20

    vida_pikachu = VIDA_INICIAL_PIKACHU
    vida_squirtle = VIDA_INICIAL_SQUIRTLE

    while vida_pikachu > 0 and vida_squirtle > 0:
        os.system("cls")
        print("""\
        ,___          .-;'
       `"-.`\_...._/`.`
    ,      \        /
 .-' ',    / ()   ()\\ 
`'._   \  /()    .  (|
    > .' ;,     -'-  /
   / <   |;,     __.;
   '-.'-.|  , \    , \\
      `>.|;, \_)    \_)
       `-;     ,    /
          \    /   <
           '. <`'-,_)
            '._)\\
        """)
        # Turno Pikachu
        print("Turno de Pikachu")
        ataque_pikachu = random.randint(1,2)
        if ataque_pikachu == 1:
            print("Pikachu ataca con Bola Voltio")
            vida_squirtle -= 10
        else:
            print("Pikachu ataca con Onda Trueno")
            vida_squirtle -= 11

        if vida_squirtle < 0:
            vida_squirtle = 0

        barra_pikachu = int((LON_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
        barra_squirtle = int((LON_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
        print("Pikachu:  [{}{}] ({}/{})".format("#" * barra_pikachu,  " " * (LON_BARRA - barra_pikachu),  vida_pikachu,  VIDA_INICIAL_PIKACHU))
        print("Squirtle: [{}{}] ({}/{})".format("#" * barra_squirtle, " " * (LON_BARRA - barra_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        print()

        if vida_pikachu < 0 or vida_squirtle < 0:
            break

        # Turno Squirtle
        print("Turno de Squirtle")
        ataque_squirtle = 'Z'  # None
        while ataque_squirtle.upper() not in ['P', 'A', 'B', 'N']:
            ataque_squirtle = input("¿Qué ataque quieres realizar? [P]lacaje, Pistola [A]gua, [B]urbuja [N]ada> ")

        if ataque_squirtle.upper() == "P":
            print("Squirtle ataca con Placaje")
            vida_pikachu -= 10
        elif ataque_squirtle.upper() == "A":
            print("Squirtle ataca con Pistola de Agua")
            vida_pikachu -= 12
        elif ataque_squirtle.upper() == "B":
            print("Squirtle ataca con Burbuja")
            vida_pikachu -= 9
        elif ataque_squirtle.upper() == "N":
            print("Squirtle no ataca en este turno")

        if vida_pikachu < 0:
            vida_pikachu = 0

        barra_pikachu = int((LON_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
        barra_squirtle = int((LON_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
        print("Pikachu:  [{}{}] ({}/{})".format("#" * barra_pikachu,  " " * (LON_BARRA - barra_pikachu),  vida_pikachu,  VIDA_INICIAL_PIKACHU))
        print("Squirtle: [{}{}] ({}/{})".format("#" * barra_squirtle, " " * (LON_BARRA - barra_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        print("Any key to continue")
        waiting = readchar.readchar().decode()

    if vida_pikachu > vida_squirtle:
        print(banner_battle_lost)
        waiting = readchar.readchar().decode()
        print("Any key to continue")
        return("Gana Pikachu")
    else:
        print(banner_battle_won)
        print("Any key to continue")
        waiting = readchar.readchar().decode()
        return("Gana Squirtle")



MAZE = """\
#############  ##########  #
#                          #
#  ##  ######  ########    #
#  ##      ##  ##          #
#  ######  ##  ##  #########
           ##  ##           
#############  #############
               ##           
#  ##############  #########
#                  ##      #
#  ##################  ##  #
#                      ##  #
#############  ##########  #\
"""

os.system("cls")
print(banner)
print("             'e' for easy mode or ANY other key to start")
mode = readchar.readchar().decode()
WALLS_KILL = (mode != "e")
os.system("cls")

# Create obstacle map
WALLS = [list(row) for row in MAZE.split("\n")]

POS_X = 0
POS_Y = 1
MAP_WIDTH = len(WALLS)
MAP_HEIGHT = len(WALLS[0])
OBJECT_NUMBER = 20
ENEMY_NUMBER = 3  # of the OBJECT_NUMBER, these are Pokemon enemies (Squirtles). You have to win these many.
DEBUG = False

my_position = [1, 1]  # x,y
snake = [[my_position[POS_X], my_position[POS_Y]]]  # The Snake is at least one element long
map_objects = []  # We'll fill it up first time we enter main()
victories = 0

# Main Loop
while victories < ENEMY_NUMBER:
    os.system("cls")

    # Generate all random objects, regenerate missing ones
    while len(map_objects) < OBJECT_NUMBER:
        obj_pos = [random.randint(1, MAP_WIDTH-1), random.randint(1, MAP_HEIGHT-1)]
        if obj_pos != my_position and obj_pos not in map_objects and WALLS[obj_pos[POS_X]][obj_pos[POS_Y]] != "#":
            map_objects.append(obj_pos)

    # Draw Map
    print("+" + "-" * (MAP_WIDTH*3) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            if [coordinate_x, coordinate_y] in snake:
                char_to_draw = " @ "
            elif [coordinate_x, coordinate_y] in map_objects:
                if map_objects.index([coordinate_x, coordinate_y]) < ENEMY_NUMBER:
                    char_to_draw = " X "
                else:
                    char_to_draw = " * "
            elif WALLS[coordinate_x][coordinate_y] == "#":
                char_to_draw = "###"
            else:
                char_to_draw = "   "
            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * (MAP_WIDTH*3) + "+")
    print("Victories: {}/{}".format(victories, ENEMY_NUMBER))

    if DEBUG:
        print("({},{}) - OBJECTS: {} - SNAKE: {}".format(my_position[POS_X], my_position[POS_Y], map_objects, snake))

    # Ask user where he wants to go

    old_position = my_position.copy()
    direction = readchar.readchar().decode()
    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "0":
        break
    else:
        my_position = old_position.copy()
        continue

    # World is a Donut/Torus
    my_position[POS_X] %= MAP_WIDTH
    my_position[POS_Y] %= MAP_HEIGHT

    if WALLS[my_position[POS_X]][my_position[POS_Y]] == "#":
        if WALLS_KILL:
            print(banner_lost)
            break
        else:
            my_position = old_position.copy()
            continue

    if my_position in map_objects:
        snake.insert(0, [my_position[POS_X], my_position[POS_Y]])
        if map_objects.index(my_position) < ENEMY_NUMBER:
            result = battle()
            if result == "Gana Pikachu":
                print(banner_lost)
                break
            else:
                victories += 1
        map_objects.remove([my_position[POS_X], my_position[POS_Y]])
    elif my_position in snake:
        print(banner_lost)
        break
    else:
        snake.insert(0, [my_position[POS_X], my_position[POS_Y]])
        snake.pop()

if victories >= ENEMY_NUMBER:
    print(banner_win)
else:
    print(banner_lost)
