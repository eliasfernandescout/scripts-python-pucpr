ano_nascimento = int(input("Digite o ano de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento (1 a 12): "))

idade = 2023 - ano_nascimento

if mes_nascimento > 4:
    idade -= 1

print("Em 2023 você terá", idade, "anos.")

if idade >= 18:
    print("Você já pode fazer a carteira de motorista!")
else:
    print("Você ainda não pode fazer a carteira de motorista.")
