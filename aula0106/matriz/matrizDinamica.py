import random

matriz = []

for linha in range(5):
    vetor = []
    for j in range(3):
        vetor.append(random.randint(0,50))
    matriz.append(vetor)

for vetor in matriz:
    print(vetor)
