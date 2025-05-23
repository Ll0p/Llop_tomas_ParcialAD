def mostrar_productos_y_ventas_decorado(ventas: list, productos: list, lista_totales: list) -> None:
    """ Muestra la matriz decorada

    Argumentos:
        ventas (list): Una matriz a recorrer
        productos (list): Lista de nombres de los productos de cada fila
        lista_totales (list): Lista con las sumas de cada filas
    """
    print("P | T1 | T2 | T3 | Total")
    print("-" * 24)
    for i in range(len(ventas)):
        print(productos[i], end=" | ")
        for j in range(len(ventas[i])):
            print(ventas[i][j], end=" | ")
        print(lista_totales[i])

def devolver_totales_ventas(ventas: list) -> list:
    """ Devuelve una lista con las sumas de cada fila

    Argumentos:
        ventas (list): Una matriz a recorrer

    Retorno:
        lista de totales (list): Retorna una lista con las sumas de cada filas
    """
    totales_ventas = []
    for i in range(len(ventas)):
        acum = 0
        for j in range(len(ventas[i])):
            acum += ventas[i][j]
        totales_ventas.append(acum)
    return totales_ventas

def ordenar_ventas_desc(ventas: list, productos: list, lista_totales: list) -> None:
    """ Ordena la matriz por el total de fila de manera descendente

    Argumentos:
        ventas (list): Una matriz a recorrer
        productos (list): Lista de nombres de los productos de cada fila
        lista_totales (list): Lista con las sumas de cada filas
    """
    for i in range(len(lista_totales) - 1):
        for j in range(i + 1, len(lista_totales)):
            if lista_totales[i] < lista_totales[j]:
                aux = lista_totales[i]
                lista_totales[i] = lista_totales[j]
                lista_totales[j] = aux

                aux = ventas[i] 
                ventas[i] = ventas[j]
                ventas[j] = aux

                aux = productos[i] 
                productos[i] = productos[j]
                productos[j] = aux

def verificar_producto(productos: list, producto: str) -> bool:
    """ Verifica si existe una cadena ingresada (producto) en una lista

    Argumentos:
        productos (list): Lista de nombres de los productos de cada fila
        producto (str): Cadena ingresada a verificar su existencia

    Retorno:
        existencia (bool): Retorna True si el producto ingresado existe en la lista
    """
    existencia = False
    for i in range(len(productos)):
        if productos[i] == producto:
            existencia = True
            break
    return existencia

def pedir_nombre_producto() -> str:
    """ Pide un nombre del producto al usuario

    Retorno:
        producto (str): Retorna la cadena ingresada en mayusculas
    """
    producto = input("Cuál producto desea buscar?: ").upper()
    return producto

def encontrar_posicion_producto(productos: list, producto: str) -> int:
    """ Encuentra la posición de un producto ingresado (asumiendo su existencia)

    Argumentos:
        productos (list): Lista de nombres de los productos de cada fila
        producto (str): Cadena ingresada a verificar su posición

    Retorno:
        posicion (int): Retorna un entero con la posicion en la lista de productos
    """
    posicion = 0
    for i in range(len(productos)):
        if productos[i] == producto:
            posicion = i
            break
    return posicion

# VERIFICAR
def mostrar_ventas_de_x_producto(ventas: list, posicion: int, productos: list, lista_totales: list) -> None:
    """ Muestra todas las ventas de un producto especifico (asumiendo su existencia) con decoracion

    Argumentos:
        ventas (list): Una matriz a recorrer
        posicion (int): Un entero con la posicion en la lista de productos
        productos (list): Lista de nombres de los productos de cada fila
        lista_totales (list): Lista con las sumas de cada filas
    """
    print("P | T1 | T2 | T3 | Total")
    print("-" * 24)
    for i in range(len(ventas)):
        if i == 0:
            print(productos[posicion], end=" | ")
        print(ventas[posicion][i], end=" | ")

        if i == (len(ventas) - 1):
            print(lista_totales[posicion], end="")
    print()

def ingresar_monto() -> int:
    """ Pide un entero (monto) al usuario

    Retorno:
        monto (int): Numero entero (que representa un monto)
    """
    monto = int(input("Qué monto desea buscar: "))
    return monto

def verificar_monto(ventas: list, monto: int) -> bool:
    """ Verifica la existencia de un entero (monto) en la matriz de ventas

    Argumentos:
        ventas (list): Una matriz a recorrer
        monto (int): Numero entero (que representa un monto)

    Retorno:
        existencia (bool): Retorna True si el monto ingresado existe en la matriz de ventas
    """
    existencia = False
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == monto:
                existencia = True
                break
        if existencia:
            break
    return existencia

def encontrar_posiciones_monto(ventas: list, monto: int) -> list:
    """ Encuentra la posiciones de un monto (asumiendo su existencia) en la matriz de ventas

    Argumentos:
        ventas (list): Una matriz a recorrer
        monto (int): Numero entero (que representa un monto ya verificado)

    Retorno:
        lista_posiciones (list): Una lista con todas las posiciones de la matriz donde fue encontrado el monto 
    """
    lista_posiciones = []
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == monto:
                lista_posiciones.append([i, j])
    return lista_posiciones

def mostrar_montos(lista_posiciones: list, productos: list) -> None:
    """ Muestra todos los montos encontrados por producto y trimestre

    Argumentos:
        lista_posiciones (list): Una lista con todas las posiciones de la matriz donde fue encontrado el monto 
        productos (list): Lista de nombres de los productos de cada fila
    """
    for i in range(len(lista_posiciones)):
        print(f'Producto "{productos[lista_posiciones[i][0]]}" | Trimestre: "{lista_posiciones[i][1]+1}"')

def mostrar_mensaje_consig_1() -> None:
    """ Muestra un mensaje estetico """
    print(f"{"-" * 8} MATRIZ {"-" * 8}\n")

def mostrar_mensaje_consig_2() -> None:
    """ Muestra un mensaje estetico """
    print("-" * 55)
    print("¡La matriz de ventas fué ordenada por ventas anuales!")
    print("-" * 55)

def mostrar_mensaje_consig_3() -> None:
    """ Muestra un mensaje estetico """
    print(f"\n{"-" * 7} PRODUCTO {"-" * 7}\n")

def mostrar_mensaje_consig_4(monto: int) -> None:
    """ Muestra un mensaje estetico 
    
    Argumento: 
        monto (int): Numero entero (que representa un monto ya verificado)
    """
    print(f'\nProducto/s y trimestre/s perteneciente a "{monto}" en la matriz:\n')