# Leitura do número de minutos utilizados
minutos = int(input("Digite a quantidade de minutos utilizados: "))

# Cálculo do valor a ser pago
if minutos <= 60:
    valor = 8.00  # Valor mínimo
else:
    horas = (minutos - 60) / 60  # Horas excedentes
    fracao = (horas - int(horas)) * 4  # Fração de 15 minutos excedentes
    valor = 8.00 + (int(horas) * 1.50) + (fracao * 1.50)

# Exibição do valor a ser pago
if valor == 8.00:
    print("Valor mínimo, R$ 8,00")
else:
    print(f"Valor fracionado, R$ {valor:.2f}")
