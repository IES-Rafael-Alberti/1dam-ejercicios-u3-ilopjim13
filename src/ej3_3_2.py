"""Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, 
finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, 
finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria."""
from borrarPantalla import borrarPantalla


def mostrar_sin_repeticiones(primaria, secundaria):
    mostrar = primaria | secundaria
    mostrar = (", ".join(mostrar))
    print(f"- Los nombres de todos los alumanos sin repeticiones son: {mostrar}.")


def mostrar_repetidos(primaria, secundaria):
    mostrar = primaria & secundaria
    mostrar = (", ".join(mostrar))
    print(f"- Los nombres de todos los alumanos repetidos son: {mostrar}.")


def mostrar_no_repetidos_nivel2(primaria, secundaria):
    mostrar = primaria ^ secundaria
    mostrar = (", ".join(mostrar))
    print(f"- Los nombres de primaria que no se repiten en secundaria son: {mostrar}.")


def mostrar_incluidos(primaria, secundaria):
    mostrar = primaria <= secundaria
    if mostrar:
        print("- Todos los nombres de primaria están incluidos en secundaria.")
    else:
        print("- No todos los nombres de primaria están incluidos en secundaria.")


def nombresSecundaria():
    borrarPantalla()
    nombres = ""
    nombres_guardados = set()
    while nombres != "x":
        nombres = input("Intorducelos nombres de los alumnos de secundaria ('x' para finalizar):\n")
        if nombres != "x":
            nombres_guardados.add(nombres)
    return nombres_guardados


def nombresPrimaria():
    nombres = ""
    nombres_guardados = set()
    while nombres != "x":
        nombres = input("Intorducelos nombres de los alumnos de primaria ('x' para finalizar):\n")
        if nombres != "x":
            nombres_guardados.add(nombres)
    return nombres_guardados


def main():
    borrarPantalla()
    primaria = nombresPrimaria()
    secundaria = nombresSecundaria()
    borrarPantalla()
    mostrar_sin_repeticiones(primaria, secundaria)
    mostrar_repetidos(primaria, secundaria)
    mostrar_no_repetidos_nivel2(primaria, secundaria)
    mostrar_incluidos(primaria, secundaria)


if __name__ == "__main__":
    main()