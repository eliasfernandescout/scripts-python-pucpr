import random

numeros = [0]*10
contador = 0

while contador < 10:
    numeros[contador] = random.randint(0, 100)
    contador += 1
print(numeros)