# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
from borrarPantalla import borrarPantalla

def mostarAsignaturas(asignaturas):
    for i in asignaturas:
        print(f"{i} tiene {asignaturas[i]}")


def totalCreditos(asignaturas):
    total = 0
    for i in asignaturas:
        total += asignaturas[i]
    print(f"El total de creditos es de {total}")

def main():
    borrarPantalla()
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    mostarAsignaturas(asignaturas)
    totalCreditos(asignaturas)


if __name__ == "__main__":
    main()

