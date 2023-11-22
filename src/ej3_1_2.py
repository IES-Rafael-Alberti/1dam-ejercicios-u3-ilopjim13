# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
from borrarPantalla import borrarPantalla

def pedirAsignatura(i):
    return input(f"{i} -> ")

def asignaturas(cont):
    return tuple(pedirAsignatura(i+1) for i in range(cont))

def yoEstudio(asignatura):
    print("\nYo estudio ",end="")
    print(", ".join(asignatura))

def main():
    borrarPantalla()
    cont = int(input("Cuantas asignaturas vas a escribir? "))
    print("\nIntroduce las asignaturas que estudias: ")
    asignatura = asignaturas(cont)
    yoEstudio(asignatura)


if __name__ == "__main__":
    main()