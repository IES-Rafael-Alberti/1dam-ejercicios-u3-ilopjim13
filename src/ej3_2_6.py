# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
from borrarPantalla import borrarPantalla

def pedirNombre(datos):
    datos["nombre"] =  input("Introduce tu nombre: ")
    print(datos["nombre"])

def pedirEdad(datos):
    datos["edad"] = input("Introduce tu edad: ") 
    print(datos["edad"])

def pedirSexo(datos):
    datos["sexo"] = input("Introduce tu sexo: ")
    print(datos["sexo"])

def pedirTelefono(datos):
    datos["telefono"] = input("Introduce tu teléfono: ")
    print(datos["telefono"])

def mostrarDatos(datos):
    return (f"\n{datos['nombre']} tiene {datos['edad']} años, es {datos['sexo']} y su número de teléfono es {datos['telefono']}")

def main():
    borrarPantalla()
    datos = {}
    pedirNombre(datos)
    pedirEdad(datos)
    pedirSexo(datos)
    pedirTelefono(datos)
    print(mostrarDatos(datos))

if __name__ == "__main__":
    main()