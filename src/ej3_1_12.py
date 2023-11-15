# Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
from borrarPantalla import borrarPantalla


def mostrarProducto(matriz1, matriz2):
    for i in range(0,3):
        for j in range(0,2):
            matriz3 = matriz1[i][j] * matriz2[i][j]
            print(f"{matriz1[i][j]} x {matriz2[i][j]} = {matriz3}")

def productoLista(matriz1, matriz2):
    return tuple(matriz1[i] * matriz2[i] for i in range(len(matriz1)))


def producto(matriz1, matriz2):
    return tuple(productoLista(matriz1[i], matriz2[i]) for i in range(len(matriz1)))


def main():
    borrarPantalla()
    matriz1= ((1,2), (3,4), (5,6))
    matriz2 = ((-1,0), (0,1), (1,1))
    matriz3 = producto(matriz1, matriz2)
    mostrarProducto(matriz1, matriz2)
    print("\n El producto de estas dos matrices es: ")
    print(f"((1,2), (3,4), (5,6)) x ((-1,0), (0,1), (1,1)) = {matriz3}")

if __name__ == "__main__":
    main()