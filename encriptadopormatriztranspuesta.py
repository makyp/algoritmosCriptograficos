def encriptar(mensaje, k):
    matriz = []
    for letra in mensaje:
        if letra != ' ':
            matriz.append(letra)
    # Asegurarse de que la matriz tenga un número de elementos múltiplo de k
    while len(matriz) % k != 0:
        matriz.append(' ')
    matriz_transpuesta = []
    for i in range(k):
        columna = matriz[i::k]
        matriz_transpuesta.append(columna)
    
    # Imprimir la matriz generada
    print("Matriz generada:")
    for fila in matriz_transpuesta:
        print(fila)

    resultado = ''
    for fila in matriz_transpuesta:
        resultado += ''.join(fila)

    resultado_agrupado = ' '.join([resultado[i:i+5] for i in range(0, len(resultado), 5)])

    return resultado_agrupado

def desencriptar(mensaje_encriptado, k):
    # Eliminar espacios del mensaje encriptado
    mensaje_sin_espacios = mensaje_encriptado.replace(' ', '')
    # Obtener el número de columnas de la matriz transpuesta
    columnas = (len(mensaje_sin_espacios) // k)
    # Calcular el número de espacios necesarios en la última columna
    espacios_faltantes = k * columnas - len(mensaje_sin_espacios)
    # Crear la matriz transpuesta vacía
    matriz_transpuesta = [[''] * columnas for _ in range(k)]
    # Llenar la matriz transpuesta con el mensaje desencriptado
    indice = 0
    for j in range(k):
        for i in range(columnas):
            if espacios_faltantes > 0:
                matriz_transpuesta[j][i] = ' '
                espacios_faltantes -= 1
            else:
                matriz_transpuesta[j][i] = mensaje_sin_espacios[indice]
                indice += 1
    # Imprimir la matriz transpuesta
    print("Matriz transpuesta:")
    for fila in matriz_transpuesta:
        print(fila)
    # Leer la matriz transpuesta para obtener el mensaje desencriptado
    mensaje_desencriptado = ''
    for i in range(columnas):
        for j in range(k):
            mensaje_desencriptado += matriz_transpuesta[j][i]
    return mensaje_desencriptado

def seleccionar_accion():
    accion = input("¿Qué acción deseas realizar? (1. encriptar / 2. descifrar): ")
    if accion == "1":
        mensaje = input("Ingresa el mensaje a encriptar: ")
        k = int(input("Ingresa el número de columnas para la matriz: "))
        mensaje_encriptado = encriptar(mensaje, k)
        print("Mensaje encriptado:", mensaje_encriptado)
    elif accion == "2":
        mensaje_encriptado = input("Ingresa el mensaje encriptado: ")
        k = int(input("Ingresa el número de columnas para la matriz: "))
        mensaje_desencriptado = desencriptar(mensaje_encriptado, k)
        print("Mensaje descifrado:", mensaje_desencriptado)
    else:
        print("Acción no válida. Por favor, selecciona 'encriptar' o 'descifrar'.")

seleccionar_accion()