import random

matriz = []

for linha in range(4):
    vetor = []
    for coluna in range(4):
        vetor.append(random.randint(10,99))
    matriz.append(vetor)

for vetor in matriz:
    print(vetor)

#
# for i in range(len(matriz)):
#     print(matriz[i][i])

# print("-------------------------")
# #matriz de qualquer dimensao
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         if i == j:
#             print(matriz[i][j])



