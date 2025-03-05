import scipy.stats as stats
import math
import numpy as np

def chi_cuadrada(numeros, desde, hasta):
    n = len(numeros)
    m = math.ceil(math.sqrt(n))
    intervalos = np.linspace(desde, hasta, m + 1)

    frecuencias_observadas, _ = np.histogram(numeros, bins=intervalos)
    frecuencia_esperada = n / m  

    chi2 = sum((o - frecuencia_esperada) ** 2 / frecuencia_esperada for o in frecuencias_observadas)
    grados_libertad = m - 1
    chi2_tabla = stats.chi2.ppf(1 - 0.05, grados_libertad)
    
    return chi2, chi2_tabla

def kolmogorov_smirnov():
    # completar
    pass

def medias():
    # completar
    pass

def varianzas():
    # completar
    pass
