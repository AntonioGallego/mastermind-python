import os
import random
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [4, 3]  # x,y
snake = [[my_position[POS_X], my_position[POS_Y]]]

# Generate random objects

map_objects = []
OBJECT_NUMBER = 30
for i in range(OBJECT_NUMBER):
    obj_pos = [random.randint(1, MAP_WIDTH-1), random.randint(1, MAP_HEIGHT-1)]
    if obj_pos != my_position and obj_pos not in map_objects:
        map_objects.append(obj_pos)

# Main Loop
while True:
    # Draw Map

    print("+" + "-" * (MAP_WIDTH*3) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            #if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
            #    char_to_draw = "@"
            if [coordinate_x, coordinate_y] in snake:
                char_to_draw = "@"
            elif [coordinate_x, coordinate_y] in map_objects:
                char_to_draw = "*"
            else:
                char_to_draw = " "
            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * (MAP_WIDTH*3) + "+")
    print("({},{}) - OBJECTS: {} - SNAKE: {}".format(my_position[POS_X], my_position[POS_Y], map_objects, snake))

    # Ask user where he wants to go

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

    # World is a Donut/Torus, my solution
    # if my_position[POS_X] > MAP_WIDTH - 1:
    #     my_position[POS_X] = 0
    # if my_position[POS_X] < 0:
    #     my_position[POS_X] = MAP_WIDTH -1
    # if my_position[POS_Y] > MAP_HEIGHT -1:
    #     my_position[POS_Y] = 0
    # if my_position[POS_Y] < 0:
    #     my_position[POS_Y] = MAP_HEIGHT -1

    # World is a Donut/Torus, Nate' solution :-)
    my_position[POS_X] %= MAP_WIDTH
    my_position[POS_Y] %= MAP_HEIGHT

    if my_position in map_objects:
        snake.insert(0, [my_position[POS_X], my_position[POS_Y]])
        map_objects.remove([my_position[POS_X], my_position[POS_Y]])
        obj_pos = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]
        if obj_pos != my_position and obj_pos not in map_objects:
            map_objects.append(obj_pos)
        if len(map_objects)==0:
            print("YOU WIN!!!")
            break
    elif my_position in snake:
        print("GAME OVER")
        break
    else:
        snake.insert(0, [my_position[POS_X], my_position[POS_Y]])
        snake.pop()

    os.system("cls")
