"""Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2."""
from borrarPantalla import borrarPantalla


def conjuntos(frutas1,frutas2):
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    return set_frutas1, set_frutas2


def conjuntosComunes(set_frutas1, set_frutas2):
    frutas_comunes = set_frutas1 & set_frutas2
    frutas_comunes = ', '.join(frutas_comunes)
    print(f"Las frutas comunes son: {frutas_comunes}.")


def soloFrutas1(set_frutas1, set_frutas2):
    frutas_solo_en_frutas1= set_frutas1 - set_frutas2
    frutas_solo_en_frutas1= ', '.join(frutas_solo_en_frutas1)
    print(f"Las frutas que están en frutas1 pero no en frutas2 son: {frutas_solo_en_frutas1}.")


def soloFrutas2(set_frutas1, set_frutas2):
    frutas_solo_en_frutas2= set_frutas2 - set_frutas1
    frutas_solo_en_frutas2= ', '.join(frutas_solo_en_frutas2)
    print(f"Las frutas que están en frutas2 pero no en frutas1 son: {frutas_solo_en_frutas2}.")


def main():
    borrarPantalla()
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1, set_frutas2 = conjuntos(frutas1,frutas2)
    conjuntosComunes(set_frutas1, set_frutas2)
    soloFrutas1(set_frutas1, set_frutas2)
    soloFrutas2(set_frutas1, set_frutas2)


if __name__ == "__main__":
    main()