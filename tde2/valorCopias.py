num_copias = int(input("Digite o número de cópias que deseja fazer: "))

if num_copias < 0:
    print("Valor inválido. O número de cópias deve ser maior ou igual a zero.")
elif num_copias < 100:
    preco = num_copias * 0.25
    print("O preço total a pagar é R$", preco)
else:
    preco = num_copias * 0.20
    print("O preço total a pagar é R$", preco)
