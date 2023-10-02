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
    resultado = ''
    for fila in matriz_transpuesta:
        for i in range(0, len(fila), 5):
            grupo = fila[i:i+5]
            resultado += ''.join(grupo) + ' '
    return resultado.strip()

def desencriptar(mensaje_encriptado):
    # Eliminar los espacios en blanco del mensaje encriptado
    mensaje_encriptado = mensaje_encriptado.replace(' ', '')
    # Obtener la longitud del mensaje encriptado
    num_caracteres = len(mensaje_encriptado)
    # Encontrar todos los posibles valores de K que pueden ser divisores de num_caracteres
    posibles_k = []
    for i in range(1, num_caracteres):
        if num_caracteres % i == 0:
            posibles_k.append(i)
    # Recorrer cada posible valor de K y tratar de desencriptar el mensaje
    for k in posibles_k:
        # Calcular el número de filas en la matriz
        num_filas = num_caracteres // k
        # Crear una matriz vacía para guardar los caracteres desencriptados
        matriz_desencriptada = [[''] * k for _ in range(num_filas)]
        # Llenar la matriz desencriptada con los caracteres del mensaje encriptado
        indice_caracter = 0
        for j in range(k):
            for i in range(num_filas):
                matriz_desencriptada[i][j] = mensaje_encriptado[indice_caracter]
                indice_caracter += 1
        # Construir el mensaje desencriptado a partir de la matriz desencriptada
        mensaje_desencriptado = ''
        for i in range(num_filas):
            for j in range(k):
                mensaje_desencriptado += matriz_desencriptada[i][j]
        # Comprobar si el mensaje desencriptado parece ser legible
        # por ejemplo, puede buscar ciertas palabras clave o patrones
        # Si encuentra una coincidencia, puede asumir que el valor de K es correcto y salir del bucle
        if 'palabra_clave' in mensaje_desencriptado:
            break
    return mensaje_desencriptado

def desencriptar(mensaje_encriptado):
    # Obtener la longitud del mensaje encriptado
    num_caracteres = len(mensaje_encriptado)
    # Encontrar el valor entero más cercano de k
    k = round(num_caracteres / int(input("Ingresa el número de columnas para la matriz: ")))
    # Calcular el número de columnas en la matriz
    num_columnas = num_caracteres // k
    # Crear una matriz vacía para guardar los caracteres desencriptados
    matriz_desencriptada = [[''] * num_columnas for _ in range(k)]
    # Llenar la matriz desencriptada con los caracteres del mensaje encriptado
    indice_caracter = 0
    for j in range(num_columnas):
        # Leer la columna de arriba hacia abajo si el índice de columna es par
        if j % 2 == 0:
            for i in range(k):
                matriz_desencriptada[i][j] = mensaje_encriptado[indice_caracter]
                indice_caracter += 1
        # Leer la columna de abajo hacia arriba si el índice de columna es impar
        else:
            for i in range(k-1, -1, -1):
                matriz_desencriptada[i][j] = mensaje_encriptado[indice_caracter]
                indice_caracter += 1
    # Construir el mensaje desencriptado a partir de la matriz desencriptada
    mensaje_desencriptado = ''
    for i in range(k):
        for j in range(num_columnas):
            mensaje_desencriptado += matriz_desencriptada[i][j]
    return mensaje_desencriptado
   
def seleccionar_accion():
    accion = input("¿Qué acción deseas realizar? (encriptar / descifrar): ")
    if accion == "encriptar":
        mensaje = input("Ingresa el mensaje a encriptar: ")
        k = int(input("Ingresa el número de columnas para la matriz: "))
        mensaje_encriptado = encriptar(mensaje, k)
        print("Mensaje encriptado:", mensaje_encriptado)
    elif accion == "descifrar":
        mensaje_encriptado = input("Ingresa el mensaje encriptado: ")
        mensaje_desencriptado = desencriptar(mensaje_encriptado)
        print("Mensaje descifrado:", mensaje_desencriptado)
    else:
        print("Acción no válida. Por favor, selecciona 'encriptar' o 'descifrar'.")

seleccionar_accion()