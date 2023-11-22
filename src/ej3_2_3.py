# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

from borrarPantalla import borrarPantalla

def pedirFruta():
    try:
        fruta = input("Introduce una de estas frutas(Plátano/Manzana/Pera/Naranja): ").capitalize().replace("á","a")
    except KeyError:
        print("Esta fruta no está.")
    else:
        return fruta


def pedirKilos():
    try:
        kilos = int(input("Introduce el numero de kilos: "))
    except ValueError:
        print("Debe de ser un numero.")
    else:
        return kilos


def precioFinal(kilos, fruta, frutas):
    total = kilos * frutas[fruta]
    print(f"El precio de {fruta} con {kilos}kg es de {total}€/kg")


def main():
    borrarPantalla()
    frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = pedirFruta()
    kilos = pedirKilos()
    precioFinal(kilos, fruta, frutas)


if __name__ == "__main__":
    main()