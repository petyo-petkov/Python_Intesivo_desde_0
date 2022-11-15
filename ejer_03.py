def numerosPrimos(n):

    num_primos = []

    for x in range(1, n + 1):
        for j in range(2, x):
            if x % j == 0:
                break
        else:
            num_primos.append(x)
    print(f'Los numeros primos enrte 1 y {n} son: ', num_primos)
    return num_primos

n = int(input('Pon un numero: '))

numerosPrimos(n)
