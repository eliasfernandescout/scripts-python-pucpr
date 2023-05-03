import random

# Função para obter a jogada do jogador humano
def obter_jogada():
  while True:
    jogada = input("Digite sua jogada (pedra, papel ou tesoura): ").lower()
    if jogada in ["pedra", "papel", "tesoura"]:
      return jogada
    print("Jogada inválida, tente novamente.")

# Função para determinar o vencedor de uma partida
def determinar_vencedor(jogada1, jogada2):
  if jogada1 == jogada2:
    return "Empate"
  elif jogada1 == "pedra" and jogada2 == "tesoura":
    return "Jogador 1"
  elif jogada1 == "tesoura" and jogada2 == "papel":
    return "Jogador 1"
  elif jogada1 == "papel" and jogada2 == "pedra":
    return "Jogador 1"
  else:
    return "Jogador 2"

# Função principal do jogo
def jogar_jokenpo():
  print("Bem-vindo ao Jokenpô!")

  # Obter modalidade do jogo
  while True:
    modalidade = input("Escolha a modalidade de jogo (1 - Humano x Humano, 2 - Humano x Computador, 3 - Computador x Computador): ")
    if modalidade in ["1", "2", "3"]:
      break
    print("Modalidade inválida, tente novamente.")
  modalidade = int(modalidade)

  # Inicializar placar
  placar = {"Jogador 1": 0, "Jogador 2": 0}

  # Laço de repetição para múltiplas partidas
  while True:
    # Obter jogada dos jogadores
    if modalidade == 1:
      jogada1 = obter_jogada()
      jogada2 = obter_jogada()
    elif modalidade == 2:
      jogada1 = obter_jogada()
      jogada2 = random.choice(["pedra", "papel", "tesoura"])
      print("Jogador 2 jogou:", jogada2)
    else:
      jogada1 = random.choice(["pedra", "papel", "tesoura"])
      jogada2 = random.choice(["pedra", "papel", "tesoura"])
      print("Jogador 1 jogou:", jogada1)
      print("Jogador 2 jogou:", jogada2)

    # Determinar vencedor e atualizar placar
    vencedor = determinar_vencedor(jogada1, jogada2)
    print("Vencedor da partida:", vencedor)
    placar[vencedor] += 1
    print("Placar geral:", placar)

    # Perguntar se deseja continuar
    while True:
      resposta = input("Deseja continuar jogando? (s/n): ").lower()
      if resposta in ["s", "n"]:
        break
      print("Resposta inválida, tente novamente.")
    if resposta == "n":
      break

  # Exibir placar final e mensagem de agradecimento
  print("Placar final:", placar)
  print("Obrig
