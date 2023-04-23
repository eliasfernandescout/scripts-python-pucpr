# Leitura da idade da pessoa
idade = int(input("Digite a sua idade: "))

# Verificação da classe eleitoral
if idade < 16:
    classe = "Não votante"
elif idade >= 18 and idade <= 65:
    classe = "Eleitor obrigatório"
else:
    classe = "Eleitor facultativo"

# Exibição da classe eleitoral
print(f"Sua classe eleitoral é: {classe}")
