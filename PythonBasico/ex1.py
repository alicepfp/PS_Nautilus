n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
n3 = input("Digite a terceira nota: ")
media = (int(n1) + int(n2) + int(n3)) / 3

if media >= 7:
    print("Sua média foi: ", media)
    print("Aprovado")

else:
    print("Sua média foi: ", media)
    print("Reprovado")
