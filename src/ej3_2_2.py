# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
from borrarPantalla import borrarPantalla

def pedirNombre():
    return input("Introduce tu nombre: ") 

def pedirEdad():
    return input("Introduce tu edad: ") 

def pedirDireccion():
    return input("Introduce tu dirección: ")

def pedirTelefono():
    return input("Introduce tu teléfono: ") 

def datosPersonales():
    return dict([("nombre", pedirNombre()), ("edad", pedirEdad()), ("direccion", pedirDireccion()), ("telefono", pedirTelefono())])

def mostrarDatos(datos):
    return (f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}")

def main():
    borrarPantalla()
    datos = datosPersonales()
    print(mostrarDatos(datos))

if __name__ == "__main__":
    main()