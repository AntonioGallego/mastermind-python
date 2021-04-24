dolar_euro = 0.91
libra_euro = 1.18

opcion = input("¿Qué desea convertir?\n"
               "1.- Dolar-Euro\n"
               "2.- Euro-Dolar\n"
               "3.- Libra-Euro\n"
               "4.- Euro-Libra\n"
               "(1-4) > ")

if opcion=="1":
    tipo_cambio = dolar_euro
    de = "dólares"
    a = "euros"
elif opcion == "2":
    tipo_cambio = 1 / dolar_euro
    de = "euros"
    a = "dólares"
elif opcion == "3":
    tipo_cambio = libra_euro
    de = "libras"
    a = "euros"
elif opcion=="4":
    tipo_cambio = 1 / libra_euro
    de = "euros"
    a = "libras"

cantidad = int(input("¿Cuanta moneda desea cambiar? > "))
resultado = cantidad * tipo_cambio
print("Sus {} {} son {} {} a un tipo de cambio de 1:{}".format(cantidad,de,resultado,a,tipo_cambio))