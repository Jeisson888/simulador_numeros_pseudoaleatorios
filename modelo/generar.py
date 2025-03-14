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

def pcg(seed,n):

    multiplier = 6364136223846793005
    increment = 1442695040888963407
    modulus = 2**64
    state = seed
    random_numbers = []

    for _ in range(n):
        state = (state * multiplier + increment) % modulus
        xorshifted = ((state >> 18) ^ state) >> 27
        rot = state >> 59
        rand_num = (xorshifted >> rot) | (xorshifted << ((-rot) & 31))
        print(rand_num)
        print(rand_num/float(2**32))
        random_numbers.append(rand_num / float(2**32))

    return random_numbers
