import matplotlib.pyplot as plt
print("Setup terminado")
colors = ["#20BEFF","#1F77B4","#72C3DC","#D6DBDF","#5D6D7E","#1C2833","#F8F9F9"]

# HISTOGRAMA
def createHistogram(marcasClase, fa, colores=colors):
    plt.figure(figsize = (8, 4))
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    plt.bar(valores_ref_eje, fa,
            width = 1, edgecolor= "k", 
            color = colores) 
    plt.xticks(valores_ref_eje, marcasClase, fontsize = 10)
    plt.xlabel("Marcas de clase", fontsize = 15)
    plt.ylabel("Frecuencia relativa", fontsize = 15)
    plt.title("Histograma", fontsize = 20)
    plt.grid()
    plt.show()

# DIAGRAMA DE BARRAS
def createBarDiagram(marcasClase, fa, colores=colors):
    plt.figure(figsize = (8, 4)) 
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    plt.barh(valores_ref_eje, fa,
            height = 0.8, edgecolor= "k", 
            color = colores) 

    plt.gca().invert_yaxis() 
    plt.yticks(valores_ref_eje, marcasClase, fontsize = 10) 
    plt.xlabel("Frecuencia absoluta ", fontsize = 15)
    plt.ylabel("Marcas de clase", fontsize = 15) 
    plt.title("Diagrama de barras", fontsize = 20) 
    plt.grid() 
    plt.show() 

# GRAFICA DE PASTEL
def generatePieChart(marcasClase, fa, fr, colores=colors):
    if 'separaciones' in locals() or 'separaciones' in globals():
        if len(separaciones) == 0:
            print("The list exists and is empty.")
            separaciones = [0] * len(fa)

        else:
            print("The list exists and is not empty.")
    else:
        #print("The list doesn't exist.")
        separaciones = [0] * len(fa)
    # Validar lista separaciones NO TOCAR el codigo de arriba
    plt.figure(figsize = (10, 6)) # (Ancho, alto) del grafico

    plt.pie(fr,
            explode = separaciones,
            colors = colores,
            pctdistance = .8,
            counterclock = False,
            startangle = 90,
            autopct = "%0.1f%%",
            labels = marcasClase)
    plt.title("Gráfico de pastel", fontsize = 20) 
    plt.show()

# POLÍGONO DE FRECUENCIAS
def createFrequencyPolygon(marcasClase, fr, colores=colors):
    plt.figure(figsize = (8, 4))
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    datos_x = [0] + valores_ref_eje + [valores_ref_eje[-1] + 1]
    datos_y = [0] + fr + [0]

    plt.plot(datos_x, datos_y, 
         linewidth = 3, 
         color = "#1C2833", 
         linestyle = "--", 
         marker = "o", 
         markersize = 10, 
         markerfacecolor = "#20BEFF", 
         markeredgecolor = "#003DA2",
         markeredgewidth = 1.5) 

    plt.xticks(valores_ref_eje, marcasClase, fontsize = 10)  
    plt.xlabel("Marcas de clase", fontsize = 15) 
    plt.ylabel("Frecuencia relativa", fontsize = 15) 
    plt.title("Poligono de frecuencias", fontsize = 20) 
    plt.grid() 
    plt.show() 

# OJIVA
def createOjiva(marcasClase, frAcum, colores=colors):
    plt.figure(figsize = (8, 4))
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    datos_x = [0] + valores_ref_eje
    datos_y = [0] + frAcum

    plt.plot(datos_x, datos_y, 
         linewidth = 3, 
         color = "#1C2833", 
         linestyle = "--", 
         marker = "o", 
         markersize = 10, 
         markerfacecolor = "#20BEFF", 
         markeredgecolor = "#003DA2",
         markeredgewidth = 1.5) 

    plt.xticks(valores_ref_eje, marcasClase, fontsize = 10, )
    plt.xlabel("Marcas de clase", fontsize = 15) 
    plt.ylabel("Frecuencia acumulada", fontsize = 15)
    plt.title("Ojiva", fontsize = 20) 
    plt.grid() 
    plt.show()


def displayCharts(marcasClase, fa, fr, frAcum, colores=colors):
    createHistogram(marcasClase, fa, colores)
    createBarDiagram(marcasClase, fa, colores)
    generatePieChart(marcasClase, fa, fr, colores)
    createFrequencyPolygon(marcasClase,fr, colores)
    createOjiva(marcasClase, frAcum, colores)