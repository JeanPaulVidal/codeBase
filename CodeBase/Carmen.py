# Clases y Frecuencia Absoluta
def frec_abs(datos_entrada):
    datos_entrada.sort()
    clases, fa_absoluta = [], []
    for elemento in datos_entrada:
        if elemento not in clases:
            clases.append(elemento)
            fa_absoluta.append(1)
        else:        
            idx = clases.index(elemento)        
            fa_absoluta[idx] += 1
    return clases, fa_absoluta  