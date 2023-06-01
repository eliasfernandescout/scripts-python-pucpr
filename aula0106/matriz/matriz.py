matriz = [[10, 20, 30],
          [40, 50, 60],
          [70, 80, 90]]

# for vetor in matriz:
#     print(vetor)

qtdLinhas = len(matriz)
qtdColunas = len(matriz[0])

print("Quantidade de linhas = ", qtdLinhas)
print("Quantidade de colunas =", qtdColunas)
for i in range(3):
    for j in range(3):
        print(matriz[i][j])