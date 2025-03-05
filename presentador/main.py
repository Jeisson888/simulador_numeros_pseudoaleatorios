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
    0.426, 0.054, 0.022, 0.742, 0.674, 0.898, 0.641, 0.674, 0.821, 0.19,
    0.46, 0.224, 0.99, 0.786, 0.393, 0.461, 0.011, 0.977, 0.246, 0.881,
    0.189, 0.753, 0.73, 0.797, 0.292, 0.876, 0.707, 0.562, 0.562, 0.821,
    0.112, 0.191, 0.584, 0.347, 0.426, 0.057, 0.819, 0.303, 0.404, 0.64,
    0.37, 0.314, 0.731, 0.742, 0.213, 0.472, 0.641, 0.944, 0.28, 0.663,
    0.909, 0.764, 0.999, 0.303, 0.718, 0.933, 0.056, 0.415, 0.819, 0.444,
    0.178, 0.516, 0.437, 0.393, 0.268, 0.123, 0.945, 0.527, 0.459, 0.652
]

chi2, chi2_tabla = chi_cuadrada(datos_ejemplo, 0, 1) # los datos de ejemplo van de 0 a 1
print('Chi cuadrada: ' + str(chi2) + ', Chi cuadrada tabla: ' + str(chi2_tabla))
# si chi2 < chi2_tabla, los datos son buenos