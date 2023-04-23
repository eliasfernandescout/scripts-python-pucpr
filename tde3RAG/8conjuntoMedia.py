numeros = []
soma = 0
contador = 0

while contador < 10:
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    soma += numero
    contador += 1

media = soma / 10

print("A soma dos números é: ", soma)
print("A média aritmética dos números é:", media)
