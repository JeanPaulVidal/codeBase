# OBTENER DATOS PARA LA TABLA DE FRECUENCIAS
def buildFreqDist(lstDatos):
    lstDatos.sort()
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
        frecRel.append(fr)
        frecRelAc.append(fr+ultFr)
        frecAbsAc.append(fa+ultFa)
        ultFr += fr
        ultFa += fa
        
    return [clase, frecAbs, frecAbsAc, frecRel, frecRelAc]

# FORMATEAR DATOS
def formatStr(strArray):
    strArraySorted = []
    for element in strArray:
        element = element.strip()
        element = element.lower()
        strArraySorted.append(element)
    return strArraySorted;

# IMPRIMIR TABLA
from IPython.display import HTML, display
def printHTMLTable(encabezados, contenido):
    if len(encabezados) == len(contenido):
        html = "<center><table>"
        html += "<tr>"
        for header in encabezados:
            html += f"<th style='border: 1px #ccc solid; text-align: center;'>{header}</th>"
        html += "</tr>"
        rowsNum = len(contenido[0])
        for row in range(rowsNum):
            html += "<tr>"
            for col in contenido:
                html += f"<td style='border: 1px #ccc solid; text-align: center;'>{col[row]}</td>"
            html += "</tr>"
        html += "</table></center>"
        
        display(HTML(html))
    else:
        print("Verificar longitud de encabezados y contenido")

# MÉTODO PARA LLAMAR TABLA
def mostrarTablaDeFrecuencias(data):
    clases, fa, faAc, fr, frAc = buildFreqDist(data)
    printHTMLTable(["Clase", "Fa", "Fr", "Fr Ac"], [clases, fa, fr, frAc])

