# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
from borrarPantalla import borrarPantalla

def pedirFecha():
    return input("Introduce una fecha con formato (dd/mm/aaaa): ")


def listaFecha(fecha:str)->list:
    lista = fecha.split("/")
    return lista

def mostrarFecha(meses,lista):
    if int(lista[0]) < 0 or int(lista[0]) > 31:
        print("-- ERROR --")
    elif int(lista[2]) < 0 or int(lista[2]) > 3000:
        print("-- ERROR --")
    elif int(lista[1]) < 0 or int(lista[1]) > 12:
        print("-- ERROR --")
    else:
        print(f"{lista[0]} de {meses[lista[1]]} de {lista[2]}")


def main():
    borrarPantalla()
    meses = {"01": "enero", "02": "febrero", "03": "marzo", "04": "abril", "05": "mayo", "06": "junio", "07": "julio", "08": "agosto", "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"}
    fecha = pedirFecha()
    lista = listaFecha(fecha)
    mostrarFecha(meses,lista)


if __name__ == "__main__":
    main()


