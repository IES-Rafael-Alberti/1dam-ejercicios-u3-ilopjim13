# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
from borrarPantalla import borrarPantalla


def pedirDivisa():
    return input("Introduce una divisa: ")


def mostrarDivisa(divisa,divisas):
    try:
        simbolo = divisas[divisa]
    except KeyError:
        print("Esta divisa no está en el diccionario")
    else:
        print(f"Su símbolo es {simbolo}")


def main():
    borrarPantalla()
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = pedirDivisa()
    mostrarDivisa(divisa,divisas)


if __name__ == "__main__":
    main()