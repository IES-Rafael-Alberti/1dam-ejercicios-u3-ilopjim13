# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
from borrarPantalla import borrarPantalla


def eliminarLetras(abecedario):
    a = len(abecedario) - 1
    rango = len(abecedario) - 1
    for i in range(rango, -1, -3):
        del abecedario[a]
        a -= 3


def main():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    borrarPantalla()
    eliminarLetras(abecedario)
    print(abecedario)


if __name__ == "__main__":
    main()
