import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo.generar import *
from modelo.probar import *

iteraciones = 20
multiplicador = 5
semilla = 7
corrimiento = 3
modulo = 16

resultados = congruencial_lineal_multiplicativo(iteraciones, multiplicador, semilla, modulo)
print('congruencial lineal multiplicativo:')
print(resultados)

resultados = congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo)
print('congruencial lineal:')
print(resultados)

semilla = 2573
resultados = cuadrados_medios(iteraciones, semilla)
print('cuadrados medios:')
print(resultados)

datos_ejemplo = [
    0.347, 0.832, 0.966, 0.472, 0.797, 0.101, 0.696, 0.966, 0.404, 0.603,
    0.993, 0.371, 0.729, 0.067, 0.189, 0.977, 0.843, 0.562, 0.549, 0.992,
    0.674, 0.628, 0.055, 0.494, 0.494, 0.235, 0.178, 0.775, 0.797, 0.252,
    0.426, 0.054, 0.022, 0.742, 0.674, 0.898, 0.641, 0.674, 0.821, 0.190,
    0.460, 0.224, 0.990, 0.786, 0.393, 0.461, 0.011, 0.977, 0.246, 0.881,
    0.189, 0.753, 0.730, 0.797, 0.292, 0.876, 0.707, 0.562, 0.562, 0.821,
    0.112, 0.191, 0.584, 0.347, 0.426, 0.057, 0.819, 0.303, 0.404, 0.640,
    0.370, 0.314, 0.731, 0.742, 0.213, 0.472, 0.641, 0.944, 0.280, 0.663,
    0.909, 0.764, 0.999, 0.303, 0.718, 0.933, 0.056, 0.415, 0.819, 0.444,
    0.178, 0.516, 0.437, 0.393, 0.268, 0.123, 0.945, 0.527, 0.459, 0.652
]
datos_ejemplo_2 = [
    0.123, 0.987, 0.567, 0.234, 0.876, 0.456, 0.789, 0.345, 0.678, 0.000,
    0.999, 0.111, 0.888, 0.222, 0.777, 0.333, 0.666, 0.444, 0.555, 0.159,
    0.842, 0.268, 0.731, 0.379, 0.620, 0.481, 0.519, 0.953, 0.047, 0.147,
    0.853, 0.258, 0.742, 0.369, 0.631, 0.491, 0.509, 0.963, 0.037, 0.136,
    0.864, 0.279, 0.721, 0.380, 0.610, 0.470, 0.530, 0.974, 0.026, 0.168,
    0.832, 0.247, 0.753, 0.358, 0.642, 0.461, 0.539, 0.985, 0.915, 0.190,
    0.810, 0.219, 0.781, 0.327, 0.673, 0.432, 0.568, 0.942, 0.958, 0.179,
    0.821, 0.289, 0.911, 0.391, 0.609, 0.403, 0.597, 0.931, 0.069, 0.180,
    0.875, 0.290, 0.910, 0.316, 0.684, 0.414, 0.586, 0.920, 0.080, 0.170,
    0.886, 0.229, 0.971, 0.328, 0.672, 0.425, 0.575, 0.910, 0.090, 0.160
]

chi2, chi2_tabla = chi_cuadrada(datos_ejemplo, 0, 1) # los datos de ejemplo van de 0 a 1
print('Chi cuadrada: ' + str(chi2) + ', Chi cuadrada tabla: ' + str(chi2_tabla))
# si chi2 < chi2_tabla, los datos son buenos

kolmogorov_smirnov(datos_ejemplo, datos_ejemplo_2)