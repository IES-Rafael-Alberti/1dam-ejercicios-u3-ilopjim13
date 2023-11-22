# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
# 6 números de 1 a 49 + reintegro de 0 a 9
# Los 6 números deben ser únicos
from borrarPantalla import borrarPantalla


def pedirNumero(numeros):
    i = 0
    for i in range(6):
        i += 1
        numero = int(input(f"{i}-> "))
        while numero <= 0 or numero > 49:
            print("ERROR, introduce un numero entre 1 y 49")
            numero = int(input(f"{i}-> "))
        while numero in numeros:
            print("ERROR, numero ya introducido")
            numero = int(input(f"{i}-> "))
        if numero > 0 and numero <= 49:
            numeros.append(numero)


def pedirReintegro(numeros):
    reintegro = int(input("Reintegro -> "))
    while reintegro < 0 or reintegro > 9:
        print("ERROR, introduce un numero entre 0 y 9")
        reintegro = int(input("Reintegro -> "))
    if reintegro >= 0 and reintegro <= 9:
        numeros.append(reintegro)
        return reintegro


def ordenarMenorMayor(numeros, total, rango):
    o = 0
    for j in range(0, total - 1):
            if numeros[rango] > numeros[rango +1]:
                o = numeros[rango]
                numeros[rango] = numeros[rango + 1]
                numeros[rango + 1] = o
            rango += 1
    return numeros



def ordenarLista(numeros):
    total = len(numeros)
    rango = 0
    for i in range(0, len(numeros)):
        ordenarMenorMayor(numeros, total, rango)
        total -= 1
    return numeros


def MostrarLoteria(numeros):
    num = numeros[0:6]
    num2 = numeros[6:7]
    print("\nTus numeros son: ", end="")
    print(" ".join(map(str,num)))
    print("Tu reintegro es: ", end="")
    print(" ".join(map(str,num2)),"\n")
    print(numeros)


def main():
    numeros = []
    borrarPantalla()
    print("Introduce los números de la lotería: ")
    pedirNumero(numeros)
    ordenarLista(numeros)
    pedirReintegro(numeros)
    MostrarLoteria(numeros)

if __name__ == "__main__":
    main()