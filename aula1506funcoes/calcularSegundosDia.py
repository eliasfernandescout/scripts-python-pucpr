def calcular_segundos_em_um_dia():
    seg_min = 60
    min_hora = 60
    hora_dia = 24
    seg_dia = seg_min * min_hora * hora_dia
    return seg_dia

seg_em_um_dia = calcular_segundos_em_um_dia()
print("Segundos em um dia:", seg_em_um_dia)
