"""Importaciones"""
from configuracion import *
import random
from extras import *

#####################################################################################################
####################################  Funciones Juego   #############################################
#####################################################################################################

""" lee el archivo y carga en la lista 'lista_producto' todas las palabras """


def lectura():
    archivo = open("recursos/db/productos.txt", "r")  # abrimos el archivo
    lista = []  # creamos una lista vacia
    for linea in archivo:  # recorremos cada linea del archivo
        elemento = linea.split(
            ","
        )  # separamos cada linea por comas lo que devuelve una lista con 3 elementos
        sublista = [
            elemento[0],
            int(elemento[1]),
            int(elemento[2]),
        ]  # creamos una sublista con 3 elementos y los elementos 1 y 2 pasan a numero
        lista.append(sublista)  # agregamos la sublista a la lista
    archivo.close()  #  cerramos el archivo
    return lista  # devuelve la lista con todas las palabras


"""De la lista de productos elige uno al azar y devuelve una lista de 3 elementos,
 el primero el nombre del producto, el segundo si es economico o premium y el tercero el precio."""


def buscar_producto(lista_productos):
    producto_final = []  # definimos la lista vacia
    producto_elegido = random.choice(
        lista_productos
    )  # elije un producto al azar de la lista de productos
    producto_final.append(producto_elegido[0])  # agregamos el nombre del producto
    aux = random.choice(producto_elegido[1:3])  # elije si es economico o premium
    if aux == producto_elegido[1]:  # si aux es economico
        producto_final.append(" (economico)")  # agregamos el tipo de producto
    elif aux == producto_elegido[2]:  # si aux es premium
        producto_final.append(" (premium)")  # agregamos el tipo de producto
    producto_final.append(aux)  # agregamos el precio del producto
    return producto_final  # devuelve la lista con el nombre del producto, el tipo de producto y el precio


"""Elige el producto. Debe tener al menos dos productos con un valor similar"""


def dameProducto(lista_productos, margen):
    seguir = True  # Inicializamos la variable seguir en True
    while seguir:  # Mientras seguir sea True el ciclo seguirá
        producto = buscar_producto(lista_productos)  # Elegimos un producto aleatorio
        es_valido = esUnPrecioValido(
            producto[2], lista_productos, MARGEN, producto[1]
        )  # Comprobamos si el precio es valido
        if es_valido:  # Si es valido
            seguir = False  # Cambiamos el valor de seguir a False
            return producto  # Devolvemos el producto elegido


"""Devuelve True si existe el precio recibido como parametro, aparece al menos 3 veces. Debe considerar el Margen."""


def esUnPrecioValido(precio, lista_productos, margen, tipo):
    contador = 0  # Inicializamos contador en 0
    precio_valido = False  # Inicializamos precio_valido en False
    for producto in lista_productos:  # Recorremos la lista de productos
        if tipo == " (economico)":  # Si el tipo es economico
            if (
                abs(precio - producto[1]) <= margen
            ):  # Si el precio es igual o menor al margen
                contador += 1  # Incrementamos el contador
        elif tipo == " (premium)":  # Si el tipo es premium
            if (
                abs(precio - producto[2]) <= margen
            ):  # Si el precio es igual o menor al margen
                contador += 1  # Incrementamos el contador
    if contador >= 3:  # Si el contador es mayor o igual a 3
        precio_valido = True  # Actualizamos precio_valido en True
    return precio_valido  # Devolvemos precio_valido


"""Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente el producto"""


def procesar(producto_principal, producto_candidato, margen):
    if (
        producto_principal[2] == producto_candidato[2]
        or abs(producto_principal[2] - producto_candidato[2]) <= margen
    ):  # comprobamos si el precio del producto_principal es igual o dentro del margen del producto_candidato
        return producto_candidato[2]  # devolvemos el precio del producto_candidato
    else:
        return producto_candidato[2] * -1  # devuelve el valor negativo


"""Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio. De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)' para que sea mostrado en pantalla."""


def dameProductosAleatorios(producto, lista_productos, margen):
    productosConMargen = []  # Definimos la Lista de productos con margen vacia
    while (
        len(productosConMargen) < 2
    ):  # Mientras la lista de productos con margen tenga menos de 2 producto
        producto_aux = buscar_producto(
            lista_productos
        )  # Elegimos un producto aleatorio
        if (
            procesar(producto, producto_aux, margen) != 0
        ):  # Si el precio del producto es diferente a 0
            if (
                producto_aux not in productosConMargen and producto_aux != producto
            ):  # Si el producto no esta en la lista de productos con margen y no es igual al producto principal
                productosConMargen.append(
                    producto_aux
                )  # Agregamos el producto a la lista de productos con margen
    while (
        len(productosConMargen) < 6
    ):  # Mientras la lista de productos con margen tenga menos de 8 productos
        producto_aux = buscar_producto(
            lista_productos
        )  # Elegimos un producto aleatorio
        if (
            producto_aux not in productosConMargen and producto_aux != producto
        ):  # Si el producto no esta en la lista de productos con margen y no es igual al producto principal
            productosConMargen.append(
                producto_aux
            )  # Agregamos el producto a la lista de productos con margen
    random.shuffle(productosConMargen)  # Mezclamos la lista de productos con margen
    productosConMargen.insert(
        0, producto
    )  # Agregamos el producto principal al principio de la lista de productos con margen
    return productosConMargen  # Devolvemos la lista de productos con margen
