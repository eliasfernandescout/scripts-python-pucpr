import math

numero = int(input("Digite um número inteiro: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    print("Valor inválido.")
