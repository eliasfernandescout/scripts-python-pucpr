import random

matriz = []

for linha in range(4):
    vetor = []
    for j in range(4):
        vetor.append(random.randint(0,50))
    matriz.append(vetor)

for vetor in matriz:
    print(vetor)

# print(matriz[0][0])
# print(matriz[1][1])
# print(matriz[2][2])
# print(matriz[3][3])

#para uma matriz quadrada
for i in range(len(matriz)):
    print(matriz[i][i])
print("-------------------------")
#matriz de qualquer dimensao
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            print(matriz[i][j])
            matriz[i][j] = matriz[i][j] * 4
            print(matriz)



