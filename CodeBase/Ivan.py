def calcular_frecuencia_acumulada(fr_relativa):
    fa_acumulada = []
    acumulado = 0
    
    for fre in fr_relativa:
        acumulado += fre
        fa_acumulada.append(acumulado)
    
    
    return fa_acumulada 