nomes = ["Dante", "Elias", "Jhess", "Bidu"]
contador = 0

while contador < len(nomes):
    print(nomes[contador])
    contador +=1

print("----------------")
#For indexando

for index in range(len(nomes)):
    print(nomes[index])

#for por favor

print("----------------")
for valor in nomes:
    print(valor)

print("----------------")
pesos = [50, 67, 74, 102]
pesoTotal = 0

for valor in pesos:
    pesoTotal += valor
print(pesos)
print(pesoTotal)