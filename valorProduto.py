
valorProduto = float(input("Insira o valor do produto: "))
valorComDesconto = valorProduto - (valorProduto*5)/100
valorComAcrescimo = valorProduto + (valorProduto*5)/100

metodoPagamento = input("Metodo de pagamento: \n"
                        "(1): A vista \n"
                        "(2): Parcelado 2x \n"
                        "(3): Parcelado 3x \n")

valorTotal = 0
if metodoPagamento == "1":
    valorTotal = valorComDesconto
if metodoPagamento == "2":
    valorTotal = valorProduto
if metodoPagamento == "3":
    valorTotal = valorComAcrescimo
else: valorProduto

print(valorTotal)






