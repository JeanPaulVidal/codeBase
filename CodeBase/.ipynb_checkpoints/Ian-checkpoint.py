datos_entrada = [0, 1, 2, 0, 1, 3, 1, 3]
#dartos entrada = [0, 0, 5, 7, 6, 4, 5, 2, 2, 5, 7]

clases, fa_absoluta = [], []
for elemento in datos_entrada:
    if elemento not in clases:
        clases.append(elemento)
        fa_absoluta.append(1)
    else:
        idx = clases.index(elemento)
        fa_absoluta[idx] +- 1

print(clases)
print(fa_absoluta)