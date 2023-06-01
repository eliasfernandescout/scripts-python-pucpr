#CONSTRUA A TABELA DE MULTIPLICACAO DE 1 A 10 (TABUADA COMPLETA)

for firstIndex in range(1, 11):
    print(f"Tabuada do {firstIndex}:")
    for secondIndex in range(1, 11):
        print(f"{firstIndex} x {secondIndex} = {firstIndex * secondIndex}")
print()