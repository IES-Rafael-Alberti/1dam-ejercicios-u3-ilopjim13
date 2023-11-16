""" Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de 
cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar 
una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea 
pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla 
la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""
from borrarPantalla import borrarPantalla


def mostrarFacturas(factura):
    print("Facturas pendientes de cobro:")
    for i in factura:
        print(f"{i} = {factura[i]}")


def pagarFactura(factura):
    pagar = input("Escriba el numero de la factura que desea cobrar: ")
    pagado = factura[pagar]
    factura.pop(pagar)
    print(f"Has cobrado {pagado}€")
    input("Enter para aceptar")


def anadirFactura(factura):
    nuevaFactura = input("Introduce una nueva factura: ")
    
    print(f"{nuevaFactura} = {factura[nuevaFactura]}")


def totalFactura(factura):
    total = 0
    for i in factura:
        total += factura[i]
    print(f"Aún te queda por cobrar un total de {total}€")


def opcionesFactura(factura):
    opcion = 1
    while opcion == 3 or opcion == 1 or opcion == 2:
        borrarPantalla()
        mostrarFacturas(factura)
        print("\n¿Qué quieres hacer?\n1) Añadir una nueva factura\n2) Pagar una factura\n3) Terminar")
        opcion = int(input(""))
        if opcion == 1:
            anadirFactura(factura)
        if opcion == 2:
            pagarFactura(factura)
        if opcion == 3:
            totalFactura(factura)
            opcion += 1


def main():
    borrarPantalla()
    factura = {"22": 50, "12":10}
    opcionesFactura(factura)



if __name__ == "__main__":
    main()