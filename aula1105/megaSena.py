import random

resultadoSorteio = []

contador= 0

while contador < 6:
    resultadoSorteio.append(random.randint(1, 60))

print(resultadoSorteio)