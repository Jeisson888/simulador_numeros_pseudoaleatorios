import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo import generar

iteraciones = 20
multiplicador = 5
semilla = 7
corrimiento = 3
modulo = 16

resultados = generar.congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo)
print(resultados)
