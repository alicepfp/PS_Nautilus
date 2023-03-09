n1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
n2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
al = ["aluno1", "aluno2", "aluno3", "aluno4", "aluno5", "aluno6", "aluno7", "aluno8", "aluno9", "aluno10"]

def listaresultados(listn1, listn2, listn3, listal):
    for i in range(10):
        media = (listn1[i] + listn2[i] + listn3[i])/3
        if media >=7:
            print(listal[i],":Aprovado")
        else:
            print(listal[i],":Reprovado")

listaresultados(n1, n2, n3, al)
