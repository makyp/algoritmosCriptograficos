def encriptar_frase(frase):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    frase_encriptada = ''
    
    for letra in frase:
        if letra.isalpha():
            # Obtener el índice de la letra en el alfabeto
            indice = alfabeto.index(letra.lower())
            # Encriptar la letra utilizando el alfabeto al revés
            letra_encriptada = alfabeto[::-1][indice]
            # Mantener el caso original de la letra
            if letra.isupper():
                letra_encriptada = letra_encriptada.upper()
            frase_encriptada += letra_encriptada
        else:
            # Mantener caracteres no alfabéticos sin encriptar
            frase_encriptada += letra
    
    return frase_encriptada


continuar = True

while continuar:
    # Solicitar al usuario que ingrese una frase
    frase_usuario = input("Ingresa una frase: ")
    
    # Encriptar la frase ingresada por el usuario
    frase_encriptada = encriptar_frase(frase_usuario)
    
    # Imprimir la frase encriptada
    print("Frase encriptada:", frase_encriptada)
    
    respuesta = input("¿Deseas realizar otra encriptación? (s/n): ")
    
    if respuesta.lower() != 's':
        continuar = False