# CLASES ORDENADAS
def get_clases(arreglo_1):
    clases = []
    for elemento in arreglo_1:
        if elemento not in clases:
            clases.append(elemento)
    
    for i in range(len(clases)):
        for j in range(i + 1, len(clases)):
            if clases[j] > clases[j]:
                clases[i], clases[j] = clases[j], clases[i]
    
    return clases
