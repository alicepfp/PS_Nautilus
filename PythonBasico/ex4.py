listaprimos = []

for i in range(2, 1001):
    divisor=0
    for j in range(2, i):
        if i % j == 0:
            divisor += 1
    if divisor == 0 or i == 2:
        listaprimos.append(i)

print("Numeros primos: ", listaprimos)
