# TABLA HTML
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


# Frecuencia absoluta
def frecAbs(lstDatos):
    lstDatos.sort()
    clase, frecAbs = [], []
    for element in lstDatos:
        if(element not in clase):
            clase.append(element)
            frecAbs.append(1)
        else:
            frecAbs[clase.index(element)] += 1
    return clase, frecAbs

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

def formatStr(strArray):
    strArraySorted = []
    for element in strArray:
        element = element.strip()
        element = element.lower()
        strArraySorted.append(element)
    return strArraySorted;

#def clasesStrSort():
#    a=1

def mostrarTabla(datos):
    datos2 = formatStr(datos)
    clases, fa = frecAbs(datos2)
    fr = frecRel(fa)
    frAc = frecAc(fr)
    printHTMLTable(["Clase",  "Fr", "Fr Ac"], [clases, fr, frAc])