import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo.generar import *

iteraciones = 20
multiplicador = 5
semilla = 7
corrimiento = 3
modulo = 16

resultados = congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo)
print(resultados)

semilla = 2573
resultados = cuadrados_medios(iteraciones, semilla)
print(resultados)
