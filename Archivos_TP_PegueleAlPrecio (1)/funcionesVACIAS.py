from principal import *
from configuracion import *
import random
import math
from extras import *

# lee el archivo y carga en la lista lista_producto todas las palabras

def lectura():
    productos = open("productos.txt", "r")
    aux=[]
    lista_productos=[]

    for producto in productos.readlines():
        aux.append(producto.replace("\n",""))
    for producto in aux:
        producto = producto.split(",")
        lista_productos.append(producto)
    productos.close()

    return lista_productos


#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto, el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
  lista_productos = lectura()
  producto = economico_premium(random.choice(lista_productos))
  return producto

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    producto_elegido = random.choice(lista_productos)
    producto_elegido_aux = random.choice(lista_productos)
    contador =0
    while contador <2:
        if dentro_del_margen(producto_elegido, producto_elegido_aux, margen):
          producto_elegido_aux = random.choice(lista_productos)
          contador+=1
        else:
          producto_elegido_aux = random.choice(lista_productos)

    return producto_elegido


#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
  contador = 0
  for producto in lista_productos:
    if precio >= producto[2] - margen and precio <= producto[2] + margen:
      contador += 1
      if contador >= 3:
        return True
  return False

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):
  if producto_principal != producto_candidato:
    if int(producto_principal[2]) - int(producto_candidato[2]) <= margen:
      return int(producto_candidato[2])
    else:
      return 0
  else:
    return 0

def economico_premium(producto):
  producto_final = [producto[0]]
  if random.randrange(0,2) == 0:
        producto_final.append(" economico")
        producto_final.append(producto[1])
  else:
        producto_final.append(" premium")
        producto_final.append(producto[2])
  return producto_final
#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
  lista_final = []
  producto_aux = [producto[0]]
  if random.randrange(0,2) == 0:
        producto_aux.append(" economico")
        producto_aux.append(producto[1])
  else:
        producto_aux.append(" premium")
        producto_aux.append(producto[2])
  lista_final.append(producto_aux)
  aux = producto_aux[2]
  aux1 = 0
  while aux != aux1:
    producto_random = random.choice(lista_productos)
    producto_final = economico_premium(producto_random)
    if int(producto_final[2]) == int(aux) and producto_final[0] != producto[0]:
      lista_final.append(producto_final)
      aux1 = producto_final[2]
  producto_random = random.choice(lista_productos)
  lista_final.append(economico_premium(producto_random))
  producto_random = random.choice(lista_productos)
  lista_final.append(economico_premium(producto_random))

  return lista_final



def dentro_del_margen(producto1, producto2, margen):
  if int(producto1[2]) - margen <= int(producto2[2]) <= int(producto1[2]) + margen:
    return True
  elif int(producto1[1]) - margen <= int(producto2[1]) <= int(producto1[1]) + margen:
    return True
  elif int(producto1[1]) - margen <= int(producto2[2]) <= int(producto1[1]) + margen:
    return True
  elif int(producto1[2]) - margen <= int(producto2[1]) <= int(producto1[2]) + margen:
    return True
  else:
    return False


