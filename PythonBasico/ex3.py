lista = list(range(1,1000+1))

listapar = []
listaimpar = []

for valor in lista:
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)

print("Numeros pares: ", listapar)
print("Numeros impares: ", listaimpar)
