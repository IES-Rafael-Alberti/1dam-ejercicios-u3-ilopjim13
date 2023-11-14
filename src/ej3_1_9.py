# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
from borrarPantalla import borrarPantalla


def pedirPalabra()-> tuple:
    palabra = input("Introduce una palabra: ").strip().lower()
    palabra = palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return tuple(palabra)


def contarVocales(palabra:tuple) -> tuple:
    vocales = (["a", 0],["e", 0],["i", 0],["o", 0],["u", 0])
    for i in vocales:
        i[1] = palabra.count(i[0])
    return vocales


def mostrarVocales(vocales):
    for i in range(0,len(vocales)-1):
        print(f"{vocales[i][0]} = {vocales[i][1]}")


def main():
    borrarPantalla()
    palabra = pedirPalabra()
    vocales = contarVocales(palabra)
    print("")
    print("Las vocales introducidas son: ")
    mostrarVocales(vocales)


if __name__ == "__main__":
    main()