def congruencial_lineal_multiplicativo(iteraciones, multiplicador, semilla, modulo):    
    resultados = []

    for _ in range(iteraciones):
        semilla = (multiplicador * semilla) % modulo
        numero_normalizado = semilla/ modulo
        resultados.append(numero_normalizado)

    return resultados

def congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo):
    resultados = []

    for i in range(iteraciones):
        resultado = (multiplicador * semilla + corrimiento) % modulo
        numero_normalizado = resultado / modulo
        resultados.append(numero_normalizado)
        semilla = resultado

    return resultados

def cuadrados_medios2(iteraciones, semilla):
    resultados = []
    slen = len(str(semilla))

    if slen %2 == 0:
      
      for i in range(iteraciones):
        semilla2 = semilla ** 2
        cadena = str(semilla2)

        if len(cadena) %2 != 0:
            cadena='0'+cadena
        if len(cadena) < slen:
            return "El número no tiene suficientes dígitos para extraer",slen,"centrales."
        inicio = (len(cadena) - slen) // 2
        digitos_centrales = cadena[inicio:inicio+slen]
        resultados.append(int(digitos_centrales))
        semilla = int(digitos_centrales)

    else:      
        for i in range(iteraciones):
            semilla2 = semilla ** 2
            cadena = str(semilla2)

            if len(cadena) %2 == 0:
                cadena='0'+cadena
            if len(cadena) < slen:
                return "El número no tiene suficientes dígitos para extraer",slen,"centrales."
            inicio = (len(cadena) - slen) // 2
            digitos_centrales = cadena[inicio:inicio+slen]
            resultados.append(int(digitos_centrales))
            semilla = int(digitos_centrales)

    return resultados

def pcg(seed, iterations):
    state = seed
    multiplier = 6364136223846793005
    increment = 1442695040888963407
    results = []
    
    for _ in range(iterations):
        # LCG: Actualiza el estado
        state = (state * multiplier + increment) & 0xFFFFFFFFFFFFFFFF
        
        # Permutación con desplazamientos y XOR
        shifted = ((state >> 18) ^ state) >> 27
        rot = state >> 59
        
        # Rotación circular
        result = (shifted >> rot) | (shifted << (64 - rot)) & 0xFFFFFFFFFFFFFFFF
        
        # Normalización para obtener un número entre 0 y 1
        results.append(result / 0xFFFFFFFFFFFFFFFF)
    
    return results
