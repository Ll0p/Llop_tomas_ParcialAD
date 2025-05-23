from Biblioteca.Datos import productos, ventas
from Biblioteca.Funciones import *

def main(ventas: list, productos: list) -> None:
    seguir = True
    while seguir:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar productos y ventas")
        print("2. Ordenar productos por ventas anuales")
        print("3. Buscar producto por nombre")
        print("4. Buscar monto de venta en la matriz")
        print("5. Salir\n")

        opcion = int(input("Selecciona una opción [1-5]: "))
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
            print("Opción no válida, vuelva a intentar...")
            opcion = int(input("Selecciona una opción [1-5]: "))

        print()
        if opcion == 1:
            lista_totales = devolver_totales_ventas(ventas)
            mostrar_mensaje_consig_1()
            mostrar_productos_y_ventas_decorado(ventas, productos, lista_totales)

        elif opcion == 2:
            lista_totales = devolver_totales_ventas(ventas)
            ordenar_ventas_desc(ventas, productos, lista_totales)
            mostrar_mensaje_consig_2()

        elif opcion == 3:
            nombre_producto = pedir_nombre_producto()
            while not verificar_producto(productos, nombre_producto):
                print("Producto inexistente, vuelva a intentar...")
                nombre_producto = pedir_nombre_producto()

            posicion = encontrar_posicion_producto(productos, nombre_producto)
            lista_totales = devolver_totales_ventas(ventas)
            mostrar_mensaje_consig_3()
            mostrar_ventas_de_x_producto(ventas, posicion, productos, lista_totales)

        elif opcion == 4:
            monto = ingresar_monto()
            while not verificar_monto(ventas, monto):
                print("Monto inexistente, vuelva a intentar...")
                monto = ingresar_monto()

            lista_posiciones = encontrar_posiciones_monto(ventas, monto)
            mostrar_mensaje_consig_4(monto)
            mostrar_montos(lista_posiciones, productos)

        else:
            print("¡Que tenga un buen dia!")
            seguir = False

main(ventas, productos)