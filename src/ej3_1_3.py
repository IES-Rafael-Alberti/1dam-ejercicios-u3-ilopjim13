# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

from borrarPantalla import borrarPantalla


def pedirNota(asignaturas):
    a = 0
    while a < len(asignaturas):
        try:
            print(f"Introduce la nota de {asignaturas[a][0]}:")
            nota = int(input())
        except ValueError:
            print("**ERROR** la nota debe ser entre 0 y 10")
        else: 
            if nota >= 0 and nota <= 10:
                asignaturas[a][1] = nota
                a +=1
            else:
                print("**ERROR** la nota debe ser entre 0 y 10")



def mostrarNotas(asignaturas):
    a = 0
    for i in asignaturas:
        print(f"En {asignaturas[a][0]} has sacado {asignaturas[a][1]}")
        a +=1



def main():
    borrarPantalla()
    asignaturas = [["Matemáticas", 0],["Física", 0],["Química", 0],["Historia", 0],["Lengua", 0]]
    pedirNota(asignaturas)
    borrarPantalla()
    mostrarNotas(asignaturas)

if __name__ == "__main__":
    main()