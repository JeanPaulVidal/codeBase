def sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
  

    fa_sorted = []
    for elemento in clases_sorted:
        idx = clases_originales.index(elemento)
        fa = fa_absolutas[idx]
        fa_sorted.append(fa)

    return fa_sorted