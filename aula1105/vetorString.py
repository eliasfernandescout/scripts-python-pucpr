import random

nome = input("Insira um nome: ")
contador = 0
qtdVogais = 0

# while contador < len(nome):
#     print(nome[contador])
#     contador+=1

while contador < len(nome):
    caracter = nome[contador]

    if caracter == "a" or caracter == "e":
        qtdVogais +=1
    contador+=1



