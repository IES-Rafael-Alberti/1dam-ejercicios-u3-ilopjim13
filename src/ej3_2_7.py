# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
from borrarPantalla import borrarPantalla


def cestaCompra(cesta):
    articulo = input("Introduce un articulo: ").capitalize
    while articulo != "*":
        try:
            cesta[articulo] = int(input("Introduce su precio: "))
        except ValueError:
            print("Introduce un numero.")
        else:
            articulo = input("Introduce un articulo (Pulsa '*' para terminar): ")



def mostarCesta(cesta):
    print("Tu cesta de la compra es:")
    for i in cesta:
        print(f"{i} = {cesta[i]}")


def totalCesta(cesta):
    total = 0
    for i in cesta:
        total += cesta[i]
    print(f"\nEl total de la cesta de compra es de {total}€")


def main():
    borrarPantalla()
    cesta = {}
    cestaCompra(cesta)
    borrarPantalla()
    mostarCesta(cesta)
    totalCesta(cesta)



if __name__ == "__main__":
    main()