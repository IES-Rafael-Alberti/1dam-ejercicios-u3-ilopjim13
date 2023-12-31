# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
from borrarPantalla import borrarPantalla


def pedirNota(asignaturas):
    a = 0
    for i in asignaturas:
        nota = int(input(f"Introduce la nota de {asignaturas[a][0]}: "))
        while nota < 0 or nota > 10:
            print("**ERROR** la nota debe ser entre 0 y 10")
            nota = int(input(f"Introduce la nota de {asignaturas[a][0]}: "))
        else: 
            asignaturas[a][1] = nota
        a +=1


def borrarAprobadas(asignaturas):
    for i in range(len(asignaturas) -1, -1, -1):
        if asignaturas[i][1] >= 5:
            del asignaturas[i]



def repetir(asignaturas):
    a = 0
    print("\nTienes que repetir:")
    for i in asignaturas:
        print(f"- {asignaturas[a][0]}")
        a +=1


def main():
    borrarPantalla()
    asignaturas = [["Matemáticas", 0],["Física", 0],["Química", 0],["Historia", 0],["Lengua", 0]]
    pedirNota(asignaturas)
    borrarAprobadas(asignaturas)
    repetir(asignaturas)

if __name__ == "__main__":
    main()