import math
## Autor: Maira
def rot13(texto):
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            resultado += chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= caracter <= 'Z':
            resultado += chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            resultado += caracter
    return resultado

def transposicion_columnar(texto_plano, password):
    filas = math.ceil(len(texto_plano) / len(password))
    columnas = len(password)
    
    #  Ordenar la contraseña en función de su posición en el alfabeto
    orden_password = sorted(password, key=lambda x: ord(x.lower()) - ord('a'))
    
    # Organizar el texto en una tabla, por filas
    tabla = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if i * columnas + j < len(texto_plano):
                fila.append(texto_plano[i * columnas + j])
            else:
                fila.append(' ')
        tabla.append(fila)
    
    # Paso 9: Leer el texto en función de la posición del alfabeto
    texto_cifrado = ''
    for letra in orden_password:
        columna = password.index(letra)
        for fila in tabla:
            texto_cifrado += fila[columna]
    
    return texto_cifrado

# Leer el texto plano
texto_plano = input("Ingresa el texto plano: ")

# Elegir la contraseña para la transposición
password = input("Ingresa la contraseña: ")

# Aplicar ROT-13 al texto plano
texto_plano_rot13 = rot13(texto_plano)

# Paso adicional: Imprimir el texto en ROT-13
print("Texto en ROT-13:", texto_plano_rot13)

# Generar el texto cifrado
texto_cifrado = transposicion_columnar(texto_plano_rot13, password)

# Mostrar el resultado
print("Texto cifrado:", texto_cifrado)