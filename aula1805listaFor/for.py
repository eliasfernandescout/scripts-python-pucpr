import random

# for index in range(10, 20, 2):
#     print(index)

somaPar = 0
somaImpar = 0

for index in range(4):
    numeroAleatorio = random.randint(0, 50)
    print("NUMERO ALEATORIO:", numeroAleatorio)
    if numeroAleatorio % 2 == 0:
        somaPar += numeroAleatorio
    else:
        somaImpar += numeroAleatorio

print("SOMA PAR: ", somaPar)
print("SOMA IMPAR: ", somaImpar)
print("---")
print(numeroAleatorio)
