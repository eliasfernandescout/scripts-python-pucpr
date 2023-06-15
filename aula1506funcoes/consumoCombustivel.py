distancia = float(input("Digite a distância total percorrida (em KM): "))
combustivel = float(input("Digite o volume de combustível consumido (em litros): "))


def calcularConsumo(distancia, combustivel):
    consumo_medio = distancia / combustivel
    return consumo_medio

resultadoConsumo = calcularConsumo(distancia, combustivel)
print("RESULTADO:", resultadoConsumo)

# print(calcularConsumo(distancia, combustivel))