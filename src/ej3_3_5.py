"""Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres."""
from borrarPantalla import borrarPantalla


def conjuntoPares(numeros):
    conjunto_de_pares = set()
    cont = len(numeros)
    for i in range(2, cont + 1, 2):
        conjunto_de_pares.add(i)
    return conjunto_de_pares


def conjuntoMultiplos3(numeros):
    conjunto_multiplos_de_tres = set()
    cont = len(numeros)
    for i in range(3, cont + 1, 3):
        conjunto_multiplos_de_tres.add(i)
    return conjunto_multiplos_de_tres


def pares_y_multiplos(conjunto_de_pares: set, conjunto_multiplos_de_tres: set):
    pares_y_multiplos_de_tres = conjunto_de_pares & conjunto_multiplos_de_tres
    pares_y_multiplos_de_tres = ', '.join(map(str, pares_y_multiplos_de_tres))
    mostrarConjuntos(conjunto_de_pares, conjunto_multiplos_de_tres)
    print(f"La intersección entre los conjuntos pares y multiplos_de_tres es: {pares_y_multiplos_de_tres}")


def mostrarConjuntos(conjunto_de_pares: set, conjunto_multiplos_de_tres: set):
    conjunto_de_pares = ', '.join(map(str, conjunto_de_pares))
    print(f"Los numeros pares son: {conjunto_de_pares}")
    conjunto_multiplos_de_tres = ', '.join(map(str, conjunto_multiplos_de_tres))
    print(f"Los multiplos de 3 son: {conjunto_multiplos_de_tres}")

def main():
    borrarPantalla()
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    conjunto_de_pares = conjuntoPares(numeros)
    conjunto_multiplos_de_tres = conjuntoMultiplos3(numeros)
    pares_y_multiplos(conjunto_de_pares, conjunto_multiplos_de_tres)


if __name__ == "__main__":
    main()