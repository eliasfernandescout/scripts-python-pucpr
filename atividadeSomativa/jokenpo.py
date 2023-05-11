from random import randint
from time import sleep

escolha = ("Pedra", "Papel", "Tesoura")
# armazena os dados e regras do jogo

computador = randint(0, 2)
#randint e um metodo do python que recebe 2 numeros como parametro e entre eles gera um numero randomico


perguntar = int(input('Escolha uma opcao para se jogar: [0] Pedra -- [1] Papel -- [2] Tesoura -- Digite sua escolha: '))

print("JO\n")
sleep(2)
#SLEEP e um metodo do python que recebe um numero como parametro sendo esse numero considerado como segundos a esperar para execucao da proxima linha de codigo
print("KENPOHHHHHH!!!!!\n")



print("O computador escolheu: {}".format(escolha[computador]))
print("O jogador escolheu: {}".format(escolha[perguntar]))


if computador == 0:
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")

