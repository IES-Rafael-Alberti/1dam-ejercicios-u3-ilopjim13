# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
# 6 números de 1 a 49 + reintegro de 0 a 9
# Los 6 números deben ser únicos

def pedirNumero(i):
    numero = int(input(f"{i}-> "))
    while numero <= 0 or numero > 49 or numero == "":
        print("ERROR, introduce un numero entre 1 y 49")
        numero = int(input(f"{i}-> "))
    if numero > 0 and numero <= 49:
        return numero


def pedirReintegro(numeros):
    reintegro = int(input("Reintegro -> "))
    while reintegro < 0 or reintegro > 9:
        print("ERROR, introduce un numero entre 1 y 49")
        reintegro = int(input("Reintegro -> "))
    if reintegro >= 0 and reintegro <= 9:
        reintegro = str(reintegro).join(numeros)
        return reintegro


def listaLoteria():
    numeros = list(pedirNumero(i + 1) for i in range(6))
    pedirReintegro(numeros)
    print(numeros)


def main():
    print("Introduce los números de la lotería: ")
    listaLoteria()

if __name__ == "__main__":
    main()