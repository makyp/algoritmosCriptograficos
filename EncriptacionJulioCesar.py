def cifrado_cesar(texto, k):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                resultado += chr((ord(letra) - 65 + k) % 26 + 65)
            else:
                resultado += chr((ord(letra) - 97 + k) % 26 + 97)
        else:
            resultado += letra
    return resultado

desplazamiento = 5

texto_original = input("Ingrese el texto original: ")
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)

print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)