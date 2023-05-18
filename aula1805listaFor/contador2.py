import random

numeros = []

while len(numeros) < 10:
    numeros.append(random.randint(0, 50))
print(numeros)

contador = 0

while contador < len(numeros):
    print(numeros[contador])
    contador+=1