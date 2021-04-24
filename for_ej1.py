texto = "Hola, me llamo Nate. ¿Tú como te llamas?"

espacios = 0
puntos = 0
comas = 0

for letra in texto:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Espacios: {}".format(espacios))
print("Puntos:   {}".format(puntos))
print("Comas:    {}".format(comas))

