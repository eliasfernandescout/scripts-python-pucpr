import time
print("...iniciando calculadora")
time.sleep(0.5)

tipoOperacao = input("Digire o tipo de operacao\n + SOMAR \n - SUBTRAIR \n * MULTIPLICAR\n / DIVIDIR\n")

if tipoOperacao == "+":
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    def somar(num1, num2):
        print("...calculando")
        time.sleep(0.5)
        return num1 + num2

    print("SOMA = ", somar(num1, num2))

if tipoOperacao == "-":
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    def subtrair(num1, num2):
        print("...calculando")
        time.sleep(0.5)
        return num1 - num2

    print("SUBTRACAO = ", subtrair(num1, num2))

if tipoOperacao == "*":
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    def multiplicar(num1, num2):
        print("...calculando")
        time.sleep(0.5)
        return num1 * num2

    print("MULTIPLICACAO = ", multiplicar(num1, num2))

if tipoOperacao == "/":
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    def dividir(num1, num2):
        print("...calculando")
        time.sleep(0.5)
        return num1 / num2

    print("DIVISAO = ", dividir(num1, num2))