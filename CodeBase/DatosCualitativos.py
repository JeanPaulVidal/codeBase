# FORMATEAR DATOS
def formatData(dataArray):
    dataArraySorted = []
    for element in dataArray:
        if isinstance(element, str):
            element = element.strip()
            element = element.lower()
            dataArraySorted.append(element)
        else:
            element = round(element, 3)
            dataArraySorted.append(element)
        
    return dataArraySorted;

# OBTENER DATOS PARA LA TABLA DE FRECUENCIAS
def generateQualitativeData(lstDatos):
    lstDatos.sort()
    lstDatos = formatData(lstDatos)
    clase, frecAbs = [], []
    for element in lstDatos:
        if(element not in clase):
            clase.append(element)
            frecAbs.append(1)
        else:
            frecAbs[clase.index(element)] += 1
        
    frecAbsAc, frecRel, frecRelAc = [], [], []
    frecAbsT = sum(frecAbs)
    ultFa = 0
    ultFr = 0
    for fa in frecAbs:
        fr = 100 / frecAbsT * fa
        frecRel.append(round(fr, 3))
        frecRelAc.append(round(fr+ultFr, 3))
        frecAbsAc.append(fa+ultFa)
        ultFr += fr
        ultFa += fa
    return [clase, frecAbs, frecAbsAc, frecRel, frecRelAc]