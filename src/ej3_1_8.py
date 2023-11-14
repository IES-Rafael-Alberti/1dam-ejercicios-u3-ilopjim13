# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def pedirPalabra():
    return input("Introduce una palabra: ")


def main():
    palabra = pedirPalabra()
    palabraOriginal = list(palabra)
    palabraReversa = list(palabra)
    palabraReversa.reverse()
    if palabraOriginal == palabraReversa:
        print("bieen")

if __name__ == "__main__":
    main()