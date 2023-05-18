import random

numeros = []
numeros2 = []

contador = 0
while contador < 10:
    numeroAleatorio = random.randint(0, 50)
    numeros.append(numeroAleatorio)
    contador +=1

print(numeros)

while len(numeros2) <10:
    numeros2.append(random.randint(0,50))

print(numeros2)