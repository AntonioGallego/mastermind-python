lista_numeros = []

num = None
while num != "q":
    num = input("Dame un número, 'q' para terminar > ")
    if num != "q":
        lista_numeros.append(int(num))

print(lista_numeros)
# print("El mínimo es {} y el máximo es {}".format(min(lista_numeros),max(lista_numeros)))
minimo = lista_numeros[0]
maximo = lista_numeros[0]
for num in lista_numeros:
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
print("El mínimo es {} y el máximo es {}".format(minimo, maximo))
