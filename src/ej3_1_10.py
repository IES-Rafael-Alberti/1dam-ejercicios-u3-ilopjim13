# Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
from borrarPantalla import borrarPantalla


def listaMayorMenor(lista):
    rango = 0
    mayor = 0
    for i in range(0, len(lista)-1):
            if lista[rango] > lista[rango +1] and lista[rango] > mayor:
                mayor = lista[rango]
            if lista[rango] < lista[rango +1]:
                menor = lista[rango]
            rango += 1
    print("El numero mayor es: " , mayor)
    print("El numero menor es: " , menor)


def main():
    borrarPantalla()
    lista = [50, 75, 46, 22, 80, 65, 8]
    listaMayorMenor(lista)


if __name__ == "__main__":
    main()