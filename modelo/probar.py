import scipy.stats as stats

def chi_cuadrada(numeros):
    k = max(numeros) + 1
    n = len(numeros)
    frecuencia_esperada = n / k
    chi2 = 0
    for i in range(k):
        frecuencia_observada = numeros.count(i)
        chi2 += (frecuencia_observada - frecuencia_esperada) ** 2 / frecuencia_esperada
    grados_libertad = k - 1
    p_valor = 1 - stats.chi2.cdf(chi2, grados_libertad)
    return chi2, p_valor

def kolmogorov_smirnov():
    # completar
    pass

def medias():
    # completar
    pass

def varianzas():
    # completar
    pass
