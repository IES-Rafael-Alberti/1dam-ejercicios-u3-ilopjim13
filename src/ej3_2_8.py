# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
from borrarPantalla import borrarPantalla


def pedirFrase():
    return input("Introduce una frase en español: ")


def traducirFrase(traductor, frase):
    fraseLista = frase.split(" ")
    a = 0
    for j in fraseLista:
        for i in traductor:
            if fraseLista[a] == i:
                fraseLista[a] = traductor[i]
        a += 1
    print("La frase traducida es: ", end="")
    print(' '.join(fraseLista))




def main():
    borrarPantalla()
    palabras = input('Introduce la palabra en español e ingles separadas por ":" y cada traduccion por ",": ')
    traductor = dict(palabra.split(":") for palabra in palabras.split(","))
    #traductor = {"hola":"hello", "adios":"bye", "bien":"good", "nombre":"name", "es": "is", "mi":"my"}
    frase = pedirFrase()
    traducirFrase(traductor, frase)


if __name__ == "__main__":
    main()