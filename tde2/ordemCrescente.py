num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
meio = (num1 + num2 + num3) - maior - menor

print(maior, meio, menor)
