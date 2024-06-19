# Frecuencia Relativa
def frecRel(frecAbs):
    frecRel = []
    frecAbsT = sum(frecAbs)
    for element in frecAbs:
        fr = 100 / frecAbsT * element
        frecRel.append(fr)
    return frecRel