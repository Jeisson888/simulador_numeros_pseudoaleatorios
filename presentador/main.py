import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo.generar.congruencial_lineal import generar

semilla = 7
multiplicador = 5
corrimiento = 3
modulo = 16
iteraciones = 20

resultados = generar(semilla, multiplicador, corrimiento, modulo, iteraciones)
print(resultados)
