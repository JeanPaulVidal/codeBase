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
