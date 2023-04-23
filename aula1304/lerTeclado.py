num = int(input("Digite sua nota: "))

while num > 0:
    num += num
    num = int(input("Digite uma nota valida: "))


print("Parabens, voce digitou uma nota valida!")
print("Media =", num)
