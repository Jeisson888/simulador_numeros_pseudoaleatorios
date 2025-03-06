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

def prueba_medias(numeros, alfa=0.05):
    media_observada = np.mean(numeros)
    media_esperada = 0.5  # Valor esperado para distribución uniforme [0, 1]
    desviacion_estandar = np.std(numeros, ddof=1)  # ddof=1 para corrección de Bessel
    n = len(numeros)

    # Estadístico de prueba t
    t_estadistico = (media_observada - media_esperada) / (desviacion_estandar / np.sqrt(n))

    # Valor p (prueba de dos colas)
    p_valor = 2 * (1 - stats.t.cdf(abs(t_estadistico), df=n - 1))

    # Decisión
    if p_valor < alfa:
        resultado = "Rechazar hipótesis nula (la media es diferente de 0.5)"
    else:
        resultado = "No rechazar hipótesis nula (la media es 0.5)"

    return t_estadistico, p_valor, resultado

def varianzas():
    # completar
    pass
