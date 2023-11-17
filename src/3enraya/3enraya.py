import os


#Simbolos que se mostrarán en el tablero
FICHAS = (' ', 'X', 'O')

def pulse_tecla_para_continuar():
    """ Mostrar el mensaje Presione una tecla para continuar y 
    hacer una pausa hasta que se realice la accion. """
    os.system("puse")

def borraConsola():
    """Limpiar consola."""
    os.system("cls")


def mostrar_fila(fila: list):
    """ Mostrar una fila del tablero
    :param fila: lista con la informacion de la fila a mostrar
    """
    contenido_fila = "| "
    for celda in fila:
        contenido_fila += FICHAS[celda] + " | "
    print(contenido_fila)



def mostrar_tablero(tablero: tuple):
    """ Mostrar en consola el tablero con las fichas.
    :param tablero: matriz de 3x3 con la información del tablero.
    """
    borraConsola()
    print("-" * 13)
    for fila in tablero:
        mostrar_fila(fila)
        print("-" * 13)


def crear_fila(num_columnas = 3) -> list:
    """Crear las columnas de una fila
    :param num_columnas: número de columnas 
    :return: lista con la fila generada conlos valores por defecto (0 = casilla vacía)
    """
    return list(0 for _ in range(num_columnas))


def crear_tablero(num_filas = 3)->tuple:
    """Crear el tablero
    :param num_filas: número de filas del tablero.
        (por defecto se establece el valor 3)
    :return: tupla con la matriz num_filas x num_columnas
    """
    return tuple(crear_fila() for _ in range(num_filas))


def cambiar_turno(turno: int) -> int:
    """Modificar el turno.
    :param turno: jugador que tiene el turno anterior.
    :return: jugador qur tiene el turno actual"""
    if turno % 2 == 0:
        return 1
    return 2


def pedir_posicion(fila_col: str, msj: str = "") -> int:

    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f'Elige la {fila_col} (1, 2, 3): ')) -1
            if not 0 <= pos <= 2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"**ERROR** {fila_col} no válida")
    return pos

def colocar_ficha(tablero: tuple, jugador:int):
    """Solicitar a un jugador las pociociones de la ficha que va a colocar.
    :param tablero: matriz de 3x3 con la informcaion del tablero
    :param jugador: número del jugador
    """
    pos_ficha = {'fila': None, 'columna': None}
    pos_correcta = False
    while not pos_correcta:
        pos_ficha['fila'] = pedir_posicion("fila", f"\nJugador {jugador}, coloque una ficha...")
        pos_ficha['columna'] = pedir_posicion("columna")

        pos_correcta = comprobar_casilla(tablero, pos_ficha)

        if pos_correcta:
            tablero[pos_ficha['fila']][pos_ficha["columna"]] =jugador
        else:
            pos_ficha['fila'] = pos_ficha["columna"] = None
            print("**Error** movimiento inválido")
            pulse_tecla_para_continuar()
            mostrar_tablero(tablero)


def comprobar_casilla(tablero: tuple, pos_ficha: dict) -> bool:
    """ Comprobar si la casilla sleccinada es correcta o no """
    return tablero[pos_ficha['fila']][pos_ficha['columna']] == 0


def verificar_ganador(tablero) -> tuple:
    """ Comprobar si algun jugador ha ganado. """
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            print(tablero[i][j])
    

def jugar(tablero: tuple):
    
    turno = 0
    ronda = 0
    hay_ganador = False

    while not hay_ganador:

        turno = cambiar_turno(turno)
        if turno == 1:
            ronda += 1
        
        print(f"\nRONDA {ronda}")
        print("-"* len(f"\nRONDA {ronda}")+ "\n")

        colocar_ficha(tablero, turno)
        mostrar_tablero(tablero)

        if ronda >= 3:
            ganador, hay_ganador = verificar_ganador(tablero)

        if hay_ganador:
            print(f"\n¡El jugador {ganador} ha ganado!\n")

        if ronda == 9:
            hay_ganador = True
            print('\n¡Empate!\n')


def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)


if __name__ == "__main__":
    main()