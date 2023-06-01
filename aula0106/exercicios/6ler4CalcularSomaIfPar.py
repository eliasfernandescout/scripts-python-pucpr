firstNumber = int(input("Insira o primeiro número: "))
secondNumber = int(input("Insira o segundo número: "))
thirdNumber = int(input("Insira o terceiro número: "))
fourthNumber = int(input("Insira o quarto número: "))

listNumber = []
listNumber.append(firstNumber)
listNumber.append(secondNumber)
listNumber.append(thirdNumber)
listNumber.append(fourthNumber)

soma = 0
for index in listNumber:
    if index %2 ==0:
        soma += index

print(soma)