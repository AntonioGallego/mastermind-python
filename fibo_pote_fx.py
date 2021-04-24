from random import randint


def potencia(*args):
    if len(args) == 1:
        return(int(args[0])*int(args[0]))
    elif len(args) == 2:
        res = 1
        for i in range(args[1]):
            res *= args[0]
        return res

def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def main():
    print("Fibonacci, primeros 20")
    for i in range(20):
        print("{} ".format(fibo(i)), end="")

    print()

    print("Cuadrados, primeros 20")
    for i in range(20):
        print("{} -> {} ".format(i, potencia(i)), end="")

    print()

    print("Cubos, primeros 20")
    for i in range(20):
        print("{} -> {} ".format(i, potencia(i, 3)), end="")

    print()

    print("Stress test 1")
    for i in range(20):
        base = randint(1, 10)
        exponente = randint(1, 10)
        print("{}^{} = {}   ".format(base, exponente, potencia(base, exponente)), end="")

    print()

    print("Stress test 2")
    for i in range(20):
        base = randint(1, 100)
        exponente = randint(1, 100)
        print("{}^{} = {}   ".format(base, exponente, potencia(base, exponente)), end="")


if __name__ == "__main__":
    main()