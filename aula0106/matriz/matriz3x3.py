import random

matriz = []

soma = 0
for linha in range(3):
    vetor = []
    for j in range(3):
        vetor.append(random.randint(0,50))
    matriz.append(vetor)
    soma += (linha + j)


for vetor in matriz:
    print(vetor)

for index in range(3):
    for j in range(3):
        soma += (index + j)

print("SOMA:", soma)



