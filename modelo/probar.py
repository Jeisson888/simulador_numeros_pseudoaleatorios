import scipy.stats as stats
import math
import numpy as np

def chi_cuadrada(numeros):
    n = len(numeros)
    m = math.ceil(math.sqrt(n))
    minimo, maximo = min(numeros), max(numeros)
    intervalos = np.linspace(minimo, maximo, m + 1)

    frecuencias_observadas, _ = np.histogram(numeros, bins=intervalos)
    frecuencia_esperada = n / m  

    chi2 = sum((o - frecuencia_esperada) ** 2 / frecuencia_esperada for o in frecuencias_observadas)
    grados_libertad = m - 1
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
