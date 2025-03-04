def congruencial_lineal_mixto():
    # completar
    pass

def congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo):
    resultados = []

    for i in range(iteraciones):
        resultado = (multiplicador * semilla + corrimiento) % modulo
        resultados.append(resultado)
        semilla = resultado

    return resultados

def cuadrados_medios():
    # completar
    pass

def otro_algoritmo():
    # completar
    pass
