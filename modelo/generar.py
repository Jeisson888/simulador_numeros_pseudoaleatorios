def congruencial_lineal_multiplicativo(iteraciones, multiplicador, semilla, modulo):    
    resultados = []

    for _ in range(iteraciones):
        semilla = (multiplicador * semilla) % modulo
        resultados.append(semilla)

    return resultados

def congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo):
    resultados = []

    for i in range(iteraciones):
        resultado = (multiplicador * semilla + corrimiento) % modulo
        resultados.append(resultado)
        semilla = resultado

    return resultados

def cuadrados_medios(iteraciones, semilla):
    resultados = []

    for i in range(iteraciones):
        semilla2 = semilla ** 2
        cadena = str(semilla2)
        digitos_centrales = cadena[(len(cadena) - 4) // 2 : ((len(cadena) - 4) // 2) + 4]
        resultados.append(int(digitos_centrales))
        semilla = int(digitos_centrales)

    return resultados

def otro_algoritmo():
    # completar
    pass
