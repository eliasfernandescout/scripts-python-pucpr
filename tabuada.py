# Lê um número inteiro do teclado
num = int(input("Digite um número inteiro: "))

# Inicializa o contador
i = 1

# Imprime a tabuada do número lido
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1
