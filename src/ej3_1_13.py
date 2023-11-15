# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
from borrarPantalla import borrarPantalla
import statistics

def pedirNumeros():
    return input("Introduce números separados por coma: ")
    


def listas(num):
    lista = num.split(",")
    lista2 = [int(i) for i in lista]
    print(lista2)
    media_y_Desviacion(lista2)


def media_y_Desviacion(lista2):
    media = statistics.mean(lista2)
    desviacion = statistics.stdev(lista2)
    print(f"La media es de: {round(media,2)}")
    print(f"La desviación es de: {round(desviacion,2)}")

def main():
    borrarPantalla()
    num = pedirNumeros()
    listas(num)
    


if __name__ == "__main__":
    main()