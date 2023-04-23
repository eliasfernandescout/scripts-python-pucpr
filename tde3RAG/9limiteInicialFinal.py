limiteInicial = int(input("Digite o limite inicial do intervalo aberto: "))
limiteFinal = int(input("Digite o limite final do intervalo aberto: "))

print(f"Números múltiplos de 3 entre {limiteInicial} e {limiteFinal}:")
while limiteInicial < limiteFinal:
    if limiteInicial % 3 == 0:
        print(limiteInicial)
    limiteInicial += 1
