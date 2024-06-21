# Frecuencia Relativa
def frecRel(frecAbs):
    frecRel = []
    frecAbsT = sum(frecAbs)
    for element in frecAbs:
        fr = 100 / frecAbsT * element
        frecRel.append(fr)
    return frecRel

# Frecuencia Acumulada
def frecAc(frec):
    frecAc = []
    ultVal = 0
    for element in frec:
        fAc = element
        frecAc.append(fAc+ultVal)
        ultVal += fAc
    return frecAc

import math
def clases_groped(datos):
    datos.sort()
    minVal = datos[0]
    maxVal = datos[0]
    
    for num in datos:
        if num > maxVal:
            maxVal = num
        if num < minVal:
            minVal = num
    
    rango = maxVal - minVal
    numClases = 1 + 3.3 * math.log10(len(datos))
    numClases = int(numClases)
    anchoClase = rango / numClases

    limsInf = []
    limsSup = []
    mrksClases = []
    for i in range(1,numClases+1):
        limSup = i*anchoClase
        limInf = limSup-anchoClase
        mrkClase = (limSup + limInf)/2
        limsSup.append(round(limSup, 3))
        limsInf.append(round(limInf, 3))
        mrksClases.append(round(mrkClase, 3))
    clases = list(range(1,numClases+1))
    return clases, limsInf, limsSup, mrksClases


def faGrouped(limSup, limInf, datos):
    fa = [0] * len(limInf)
    for dato in datos:
        for j in range(0, len(limInf)):
            # Para crear la otra distribucion se cambian las contidiones
            #if j == 0:
            if j == len(limInf)-1:
                if limInf[j] <= dato <= limSup[j]:
                    fa[j] += 1
                    break
            else:
                #if limInf[j] < dato <= limSup[j]:
                if limInf[j] <= dato < limSup[j]:
                    fa[j] += 1
                    break
    return fa
    
def generateGroupedData(datos):
    clases, limsInf, limsSup, mrksClases = clases_groped(datos)
    fa = faGrouped(limsSup, limsInf, datos)
    fr = frecRel(fa)
    frAc = frecAc(fr)

    return clases, limsInf, limsSup, mrksClases, fa, fr, frAc