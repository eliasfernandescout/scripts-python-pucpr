cotacao_dolar = 5.25
cotacao_libra = 7.30
cotacao_euro = 6.15

codigo_moeda = int(input("Digite o código da moeda que deseja comprar (1 - dólar, 2 - libra, 3 - euro): "))
montante = float(input("Digite o montante que deseja adquirir nessa moeda: "))

if codigo_moeda == 1:
    valor_total = cotacao_dolar * montante
    nome_moeda = "dólares"
elif codigo_moeda == 2:
    valor_total = cotacao_libra * montante
    nome_moeda = "libras"
elif codigo_moeda == 3:
    valor_total = cotacao_euro * montante
    nome_moeda = "euros"
else:
    print("Código de moeda inválido!")
    exit()

if valor_total < 1000:
    comissao = valor_total * 0.05
else:
    comissao = valor_total * 0.03

valor_total += comissao

print(f"Valor a ser pago em reais pela compra de {montante:.2f} {nome_moeda}: R$ {valor_total:.2f}")
