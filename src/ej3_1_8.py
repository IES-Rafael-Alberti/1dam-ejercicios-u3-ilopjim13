# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
from borrarPantalla import borrarPantalla

def pedirPalabra():
    return input("Introduce una palabra: ")


def main():
    borrarPantalla()
    palabra = pedirPalabra()
    palabraOriginal = list(palabra)
    palabraReversa = list(palabra)
    palabraReversa.reverse()
    if palabraOriginal == palabraReversa:
        print("Esta palabra es un políndromo")
    else:
        print("Esta palabra no es un políndromo")


if __name__ == "__main__":
    main()