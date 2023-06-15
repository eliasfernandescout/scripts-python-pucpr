def imprimir_numeros_impares():
    contador = 0
    numero = 1

    while contador < 100:
        if numero % 2 != 0:
            print(numero)
            contador += 1
        numero += 1

imprimir_numeros_impares()
