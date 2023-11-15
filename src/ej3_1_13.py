# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
from borrarPantalla import borrarPantalla

def pedirNumeros():
    return input("Introduce números separados por coma: ")
    


def lista(num):
    lista = num.split(",")
    print(lista)


def main():
    borrarPantalla()
    num = pedirNumeros()
    lista(num)


if __name__ == "__main__":
    main()