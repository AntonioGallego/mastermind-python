ARCHIVO = "compra.txt"
TIENDA = ["placa", "memoria", "fuente", "micro", "disco", "cables", "grafica", "raton", "teclado"]

def preguntar_producto():
    return input("Introduce un producto [(S)alir, (T)ienda (C)arrito (G)rabar ] > ")

def mostrar(l):
    print("\n".join(l))

def guardar_carrito(carrito):
    with open(ARCHIVO, "w") as mi_archivo:
        mi_archivo.write("\n".join(carrito))
    print("Carrito guardado en compra.txt")

def main():
    carrito = []

    print("Bienvenido a AntonioZon")
    mostrar(TIENDA)

    if input("¿Quieres cargar la ultima lista de la compra? [S/N] > ") == "S":
        try:
            with open(ARCHIVO, "r") as fic:
                carrito = fic.read().split("\n")
        except FileNotFoundError:
            print("Archivo de la compra no encontrado")


    input_usuario = preguntar_producto()
    while input_usuario != "S":
        if input_usuario == "C":
            mostrar(carrito)
        elif input_usuario == "T":
            mostrar(TIENDA)
        elif input_usuario == "G":
            guardar_carrito(carrito)
        elif input_usuario in TIENDA:
            if input_usuario.lower() not in [a.lower() for a in carrito]:
                carrito.append(input_usuario.lower())
            else:
                print("Producto duplicado")
        else:
            print("Producto no disponible")
        input_usuario = preguntar_producto()

if __name__ == "__main__":
    main()
