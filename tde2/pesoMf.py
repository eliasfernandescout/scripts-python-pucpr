altura = float(input("Digite a altura em metros: "))
sexo = int(input("Digite o sexo (1 para masculino ou 2 para feminino): "))

if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem de", altura, "metros é:", peso_ideal, "kg.")
elif sexo == 2:
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher de", altura, "metros é:", peso_ideal, "kg.")
else:
    print("Valor inválido. O sexo deve ser 1 para masculino ou 2 para feminino.")
