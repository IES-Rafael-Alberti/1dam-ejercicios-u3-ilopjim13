# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
from borrarPantalla import borrarPantalla
import statistics

def pedirNumeros():
    return input("Introduce números separados por coma: ")    


def listas(num):
    listastr = num.split(",")
    listaint = [int(i) for i in listastr]
    print(listaint)
    return listaint


def media(listaint):
    suma = 0
    division = len(listaint)
    for i in listaint:
        suma += i
    media = suma / division
    print(f"La media es de: {round(media,2)}")


def desviacion(listaint):
    desviacion = statistics.stdev(listaint)
    print(f"La desviación es de: {round(desviacion,2)}")


def main():
    borrarPantalla()
    num = pedirNumeros()
    listaint = listas(num)
    media(listaint)
    desviacion(listaint)


if __name__ == "__main__":
    main()