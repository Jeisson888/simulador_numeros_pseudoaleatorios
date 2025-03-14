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
    
    if chi2 < chi2_tabla:
        conclusion = "Los datos son buenos."
    else:
        conclusion = "Los datos no son buenos."

    mensaje = (f"Chi-cuadrado calculado: {chi2}\n"
               f"Chi-cuadrado tabla: {chi2_tabla}\n"
               f"{conclusion}")

    return mensaje

def kolmogorov_smirnov(muestra_A):
    # Prueba K-S para dos muestras
    mid = len(muestra_A)//2
    statistic, p_value = ks_2samp(muestra_A[:mid], muestra_A[mid])

    print(f'Estadística de prueba: {statistic}')
    print(f'Valor p: {p_value}')

    if p_value < 0.05:
        return('Los datos no son buenos: las muestras provienen de distribuciones diferentes.')
    else:
        return('Los datos son buenos: no hay evidencia suficiente para afirmar que las muestras provienen de distribuciones diferentes.')

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
        resultado = "Los datos no son buenos (la media es diferente de 0.5)"
    else:
        resultado = "Los datos son buenos (la media es 0.5)"

    return t_estadistico, p_valor, resultado

def varianzas (data, confidence=0.95):
    print(data)
    n = len(data)
    sample_variance = np.var(data, ddof=1)  # Varianza muestral
    print(sample_variance)
    df = n - 1  # Grados de libertad
    
    chi2_lower, chi2_upper = stats.chi2.interval(confidence, df)
    print(chi2_lower)
    print(chi2_upper)
    
    lower_bound = chi2_lower / (12*df)
    upper_bound = chi2_upper /(12*df)

    if lower_bound <= sample_variance <= upper_bound:
        return "Con nivel de confianza "+str(confidence)+" los datos son buenos ya que la varianza es igual a 1/12 "
    else:
        return "Con nivel de confianza "+str(confidence)+" los datos no son buenos ya que la varianza es diferente a 1/12 "

