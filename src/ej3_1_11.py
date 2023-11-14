# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
from borrarPantalla import borrarPantalla


def multiplicarListas(lista1, lista2):
    for i in range(len(lista1)):
        total = (lista1[i] * lista2[i])
        print(f"{lista1[i]} * {lista2[i]} = {total}")


def main():
    borrarPantalla()
    lista1= (1,2,3)
    lista2= (-1,0,2)
    multiplicarListas(lista1, lista2)


if __name__ == "__main__":
    main()