import random

numeros = []
contador = 0
somaPar = 0
somaImpar = 0
while contador < 5:
    numeros.append(random.randint(0, 50))
    contador+=1

print(numeros)

contador = 0
while contador < len(numeros):
    if numeros[contador] %2 ==0:
        somaPar += numeros[contador]
    else:
        somaImpar += numeros[contador]
    contador+=1

print(numeros)
print(somaPar)
print(somaImpar)
