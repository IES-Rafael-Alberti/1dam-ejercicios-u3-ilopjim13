""" Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave 
de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde 
preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir 
cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción 
elegida el programa tendrá que hacer lo siguiente:

- Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
- Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
- Preguntar por el NIF del cliente y mostrar sus datos.
- Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
- Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
- Terminar el programa. """
from borrarPantalla import borrarPantalla


def anadirCliente(clientes):
    borrarPantalla()
    clientes[input("Introduce el NIF del nuevo cliente: ")] = dict({"Nombre":input("Introduce su nombre: "), "Direccion":input("Su direccion: "), "Telefono":input("Su telefono: "), "Correo":input("Su correo: "), "Preferente":bool(input("Preferente (True/False): "))})


def eliminarCliente(clientes):
    borrarPantalla()
    quitar = "N"
    try:
        nif = input("Escriba el NIF del cliente que desea eliminar: ")
        while quitar != "s":
            quitar = input(f"¿Seguro que quieres eliminar el cliente con el NIF {nif}? (s/n) ").upper
            if quitar != "s":
                nif = input("Escriba el NIF del cliente que desea eliminar: ")
        clientes.pop(nif)
    except KeyError:
        print("No existe este cliente")
    input("\nPresione ENTER para volver al menu")


def mostrarCliente(clientes):
    borrarPantalla()
    try:
        nif = input("Introduce el NIF del cliente que quiere ver sus datos: ")
        print("\nSus datos son: ")
        for i in clientes[nif]:
            print(f"- {i}: {clientes[nif][i]}")
    except KeyError:
        print("No existe ningun cliente con ese NIF")
    input("\nPresione ENTER para volver al menu")


def listarClientes(clientes):
    borrarPantalla()
    print("Los clientes de la Base de Datos son: ")
    for i in clientes:
        print(f'{i} - {clientes[i]["Nombre"]}')
    input("Presione ENTER para volver al menu")


def listarClientesPreferentes(clientes):
    borrarPantalla()
    print("Los clientes preferentes de la Base de Datos son: ")
    for i in clientes:
        for j in clientes[i]:
            if clientes[i][j] == True:
                print(f'{i} - {clientes[i]["Nombre"]}')
    input("Presione ENTER para volver al menu")


def terminar():
    borrarPantalla()
    print("Adios master")
    exit()


def menuOpciones(clientes):
    opcion = 1
    while opcion != 6:
        borrarPantalla()
        print("\n¿Qué quieres hacer?\n\n1) Añadir cliente\n2) Eliminar cliente\n3) Mostrar cliente\n4) Listar todos los clientes\n5) Listar clientes preferentes\n6) Terminar")
        opcion = int(input("\nEliga --> "))
        if opcion == 1:
            anadirCliente(clientes)
        if opcion == 2:
            eliminarCliente(clientes)
        if opcion == 3:
            mostrarCliente(clientes)
        if opcion == 4:
            listarClientes(clientes)
        if opcion == 5:
            listarClientesPreferentes(clientes)
        if opcion == 6:
            terminar()
        if opcion < 1 or opcion > 6:
            print("-- ERROR -- Eliga una opción entre 1 y el 6")


def main():
    borrarPantalla()
    clientes = {"55555G": {"Nombre":"Pepe", "Direccion":"Cadiz", "Telefono":"4445556", "Correo":"Pepe@gmail.com", "Preferente":True}, "888888P": {"Nombre":"Antonio", "Direccion":"Cadiz", "Telefono":"4448856", "Correo":"Antonio@gmail.com", "Preferente":False}}
    menuOpciones(clientes)


if __name__ == "__main__":
    main()