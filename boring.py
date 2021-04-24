from random import randint


def string_mas_larga(*args):
    """Ejercicio 1: La string más larga
    Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas
    Ejemplo:
    string_mas_larga("hola", "como", "estas")
    > "estas"
    """
    longest = ""
    for item in args:
        if len(item) > len(longest):
            longest = item
    return(longest)


def suma_mejorada(*args):
    """Ejercicio 2: Sumando la lista
    Crea una función que sume una serie de argumentos
    Ejemplo:
    suma(1, 2, 3, 4, 5)
    > 15
    """
    res = 0
    for item in args:
        res += item
    return res


def suma(lista_numeros):
    """Ejercicio 2: Sumando la lista
    Crea una función que sume una lista de números, no se vale usar la función sum()
    Ejemplo:
    suma(1, 2, 3, 4, 5)
    > 15
    """
    res = 0
    for item in lista_numeros:
        res += item
    return res


def es_impar(num):
    """Ejercicio 3: Par o impar
    Crea una función que te de True como resultado si el número pasado como argumento es impar
    Ejemplo:
    es_impar(3)
    > True
    es_impar(24)
    > False
    """
    return(num%2 == 1)

def estas_seguro():
    """Ejercicio 4: pregunta algo
    Crea una función que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False" dependiendo de si el usuario está seguro.
    """
    res = input("¿Estás seguro? [S]/[N] > ")
    return res in ("S", "s", "Y", "y")

def mays(cad):
    """
    Ejercicio 5: A mayus
    Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()
    Para ello tiramos de ord y chr, que suelen formar parte de la built_in
    >>> ord("A")
    65
    >>> ord("a")
    97
    >>> ord("a")-ord("A")
    32
    >>> chr(97)
    'a'
    >>> chr(65)
    'A'
    """
    res = ""
    for letra in cad:
        if 122 >= ord(letra) >= 97:
            n = ord(letra) - 32
        else:
            n = ord(letra)
        res += chr(n)
    return res

def adivina(tope):
    """Ejercicio 6: Adivina el número
    Crea una función que reciba como argumento un número del 1 al 100 a adivinar y que le pregunte al usuario que adivine el número. El código se ejecutará hasta que el usuario adivine.
    """
    while True:
        dado = randint(1, tope)
        resp = int(input("Adivina mi número (1-{}) > ".format(tope)))
        if resp == dado:
            print("Al fin acertaste")
            return
        else:
            print("Era el {}, sigue probando".format(dado))

def add_carrito(carrito):
    """Ejercicio 7: Lista de la compra
    Crea una función que dada una lista de la compra definida fuera de la función, permita al usuario añadir un nuevo item asegurandose que no exista anteriormente en la lista.
    """
    while True:
        item = input("Que quieres añadir a la lista > ")
        if item.lower() not in carrito:
            carrito.append(item.lower())
            return
        else:
            print("{} ya está en la lista".format(item))



def main():
    print("Ejercicio 1")

    print("La cadena más larga de la lista es '{}'".format(string_mas_larga("hola", "como", "estas")))

    print("Ejercicio 2")
    print("La suma de los argumentos es {}".format(suma([1, 2, 3, 4, 5])))
    print("La funcion suma_mejorada lo hace por *args, sin listas, y da lo mismo:  {}".format(suma_mejorada(1, 2, 3, 4, 5)))

    print("Ejercicio 3")
    print(es_impar(3))
    print(es_impar(24))
    for i in range(10):
        num = randint(0,100)
        if es_impar(num):
            print("El número {} es impar. ".format(num), end="")
        else:
            print("El número {} es par. ".format(num), end="")
    print()

    print("Ejercicio 4")
    for i in range(4):
        if estas_seguro():
            print("Estoy muy seguuuuuuuuuroooooooooo")
        else:
            print("Pues asegúrate")

    print("Ejercicio 5")
    cad = """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.
    
    Ut enim ad minim veniam,
    quis nostrud exercitation
    ullamco laboris nisi ut aliquip
    ex ea commodo consequat.
     
    Duis aute irure dolor in reprehenderit
    in voluptate velit esse cillum dolore
    eu fugiat nulla pariatur.
    
    Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
    """

    print(mays(cad))

    print("Ejercicio 6")
    adivina(6) # (del 1 al número pasado, poner a 100 para seguir el enunciado al pie de la letra)

    print("Ejercicio 7")
    carrito = ['leche','pan','huevos']
    print("Esta es la lista de la compra {}".format(carrito))
    add_carrito(carrito)
    print("Esta es la nueva lista de la compra {}".format(carrito))


if __name__ == "__main__":
    main()