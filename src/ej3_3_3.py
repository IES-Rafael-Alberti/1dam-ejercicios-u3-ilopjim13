""" El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]"""
from borrarPantalla import borrarPantalla


def pedirConjunto():
    num = input("Introduce el conjunto de potencias (ej: 1,2,3): ")
    lista = num.split(",")
    s = set(lista)
    return s


#def conjunto_potencia(s):



def main():
    borrarPantalla()
    conjunto = [set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
    s = pedirConjunto()
    print('({6, 1, 4})')
    print(s)
    print(conjunto)


if __name__ == "__main__":
    main()