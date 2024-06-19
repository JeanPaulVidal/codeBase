# Imprimir tabla
def printTable(encabezados, contenido):
    '''
        Dados 2 arreglos del mismo tamaño, crea una tabla  con encabezados y contenido
        Ejemplo:
            clases = [0, 5, 7, 6, 4, 2]
            frecAbs = [2, 3, 2, 1, 1, 2]
            printTable(["Clase", "Fa"], [clases, frecAbs])
    '''
    from tabulate import tabulate
    if(len(encabezados) == len(contenido)):
        data = list(zip(*contenido))
        table = tabulate(data, headers=encabezados, tablefmt="orgtbl")
        print(table)
