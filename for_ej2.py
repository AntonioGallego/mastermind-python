import string

texto = input("Introduzca un texto > ")
letras_mayusculas = 0
for letra in texto:
    if letra.isupper():
        letras_mayusculas += 1
print("Encontradas {} mayúsculas".format(letras_mayusculas))
