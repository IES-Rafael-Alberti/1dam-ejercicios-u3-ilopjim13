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


def sector1():
    entrada = {1,2,3}
    conjunto = list()
    todo = len(entrada) * 2 + 2
    for i in range(todo):
        conjunto.append(set(str(i)))
    print(conjunto)


def numeros():
    entrada = {1,2,3}
    conjunto = list()
    cont = 1
    for j in entrada:
        for i in range(cont):
            numero = j
        conjunto.append(set(str(numero)))
        cont += 1
    print(conjunto)
    dos_en_Dos(conjunto)


def dos_en_Dos(conjunto:list):
    entrada = {1,2,3}
    cont = 1
    for j in entrada:
        for i in range(cont):
            numero = j
            numero2 = j + 1
        conjunto.append(set(str(numero)))
        cont += 1
    print(conjunto)


#def conjunto_potencia(s):



def main():
    borrarPantalla()
    numeros()
    # sector1()
    # conjunto = [set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
    # s = pedirConjunto()
    # print('({6, 1, 4})')
    # print(s)
    # print(conjunto)


if __name__ == "__main__":
    main()