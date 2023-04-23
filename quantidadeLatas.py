import math

altura = float(input("Digite a altura do cilindro em metros: "))
raio = float(input("Digite o raio do cilindro em metros: "))

area_base = math.pi * raio ** 2
area_lateral = 2 * math.pi * raio * altura
area_total = area_base + area_lateral

litros_necessarios = area_total / 3
latas_necessarias = math.ceil(litros_necessarios / 5)
valor_total = latas_necessarias * 50

print("Serão necessárias", latas_necessarias, "latas de tinta para pintar o cilindro.")
print("O valor total das latas de tinta será de R$", valor_total)
