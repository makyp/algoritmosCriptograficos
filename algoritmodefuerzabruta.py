alfabeto = "abcdefghijklmnopqrstuvwxyz"


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

def desencriptar_cesar(texto_cifrado):
    for k in range(27):
        resultado = cifrado_cesar(texto_cifrado, -k)
        print(f"Con k={k}: {resultado}")

texto_cifrado = input("Ingrese el texto cifrado: ")
desencriptar_cesar(texto_cifrado)