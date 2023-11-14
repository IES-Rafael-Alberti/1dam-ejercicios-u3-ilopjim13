# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
from borrarPantalla import borrarPantalla

def ordenInverso(lista: list):
    lista2 = lista.copy()
    lista2.reverse()
    print(", ".join(map(str, lista2)))
    print(", ".join(map(str, lista)))
    



def main():
    borrarPantalla()
    lista= [1,2,3,4,5,6,7,8,9,10]
    ordenInverso(lista)

if __name__ == "__main__":
    main()