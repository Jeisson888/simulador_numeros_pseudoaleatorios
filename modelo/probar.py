import scipy.stats as stats
import math
import numpy as np
from scipy.stats import ks_2samp

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

def kolmogorov_smirnov(muestra_A, muestra_B):
# Prueba K-S para dos muestras
    statistic, p_value = ks_2samp(muestra_A, muestra_B)

    print(f'Estadística de prueba: {statistic}')
    print(f'Valor p: {p_value}')

    if p_value < 0.05:
        print('Rechazamos la hipótesis nula: las muestras provienen de distribuciones diferentes.')
    else:
        print('No podemos rechazar la hipótesis nula: no hay evidencia suficiente para afirmar que las muestras provienen de distribuciones diferentes.')

def medias():
    # completar
    pass

def varianzas():
    # completar
    pass
