massa = float(input("Digite sua massa em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = massa / altura ** 2

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade grau I.")
elif imc < 40:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III ou mórbida.")

if imc >= 25:
    massa_max_normal = 24.9 * altura ** 2
    print("Sua massa máxima considerada normal é:", massa_max_normal, "kg")
