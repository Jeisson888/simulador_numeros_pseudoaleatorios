def generar(semilla, multiplicador, corrimiento, modulo, iteraciones):
    resultados = []

    for i in range(iteraciones):
        resultado = (multiplicador * semilla + corrimiento) % modulo
        resultados.append(resultado)
        semilla = resultado

    return resultados
