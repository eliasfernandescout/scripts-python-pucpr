import random

matriz = []

for linha in range(2):
    vetor = []
    for j in range(2):
        vetor.append(random.randint(0,50))
    matriz.append(vetor)

for vetor in matriz:
    print(vetor)

soma = 0
for linha in matriz:
    for numero in linha:
        soma += numero
print("SOMA: ", soma)