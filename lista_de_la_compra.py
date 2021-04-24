print("Programa lista de la compra")

lista_de_la_compra = []

item = None
while item != "Q":
    item = input("¿Qué desea comprar? ([Q] para salir) > ")
    if item == "Q":
        break
    if item in lista_de_la_compra:
        print("¡{} ya está en la lista!".format(item))
    else:
        confirma = None
        while confirma not in ['S','N']:
            confirma = input("¿Seguro que desea añadir {}? [S/N] > ".format(item))
        if confirma == "S":
            lista_de_la_compra.append(item)
            print("¡{} añadido!".format(item))

print("la lista de la compra es:")
print(lista_de_la_compra)