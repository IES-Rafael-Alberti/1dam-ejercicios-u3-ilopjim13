# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
from borrarPantalla import borrarPantalla

def asignaturas(asignatura):
    print(", ".join(asignatura))


def main():
    asignatura = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
    borrarPantalla()
    asignaturas(asignatura)

if __name__ == "__main__":
    main()