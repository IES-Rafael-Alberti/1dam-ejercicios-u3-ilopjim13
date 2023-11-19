""" Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes."""
from borrarPantalla import borrarPantalla


def letrasAlfabeto():
    return set(map(chr, range(97, 123)))


def consonantes_sin_vocales(vocales, alfabeto):
    consonantes = vocales ^ alfabeto
    print(consonantes)
    return consonantes

def comunes(vocales, consonantes):
    letras_comunes = vocales & consonantes
    print(letras_comunes)


def main():
    borrarPantalla()
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = letrasAlfabeto()
    consonantes = consonantes_sin_vocales(vocales, alfabeto)
    comunes(vocales, consonantes)


if __name__ == "__main__":
    main()