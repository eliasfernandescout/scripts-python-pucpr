import random

vetor = []

for i in range(10):
    vetor.append(random.randint(0,10))

print(vetor)

valor = int(input("Digite um número: "))
repeticoes = 0
for i in range(len(vetor)):
    if vetor[i] == valor:
        print(i)
        repeticoes +=1
print("repeticoes: ", repeticoes)