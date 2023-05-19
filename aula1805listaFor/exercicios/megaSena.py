import random

numerosSorteados = []
numerosDigitados = []

for i in range(6):
    numeroAleatorio = random.randint(1, 60)
    while numeroAleatorio in numerosSorteados:
        numeroAleatorio = random.randint(1, 60)
    numerosSorteados.append(numeroAleatorio)

for i in range (6):
    numDigitado