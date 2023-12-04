import pygame
from pygame.locals import *
from configuracion import *

"""define la funcion dameLetraApretada que devuelve una cadena con la letra apretada en el teclado"""
def dameLetraApretada(key): # Devuelve una cadena con la letra apretada
  if K_0 <= key <= K_9: # Si son numeros del 0 al 9
    return str(key - K_0) # Convierte el valor a cadena
  else: # Cualquier otra tecla
    return "" # Devuelve cadena vacia

#####################################################################################################
#  Funciones Juego
#####################################################################################################

""" define la funcion dibujar que dibuja el juego"""
def dibujar(screen, productos_en_pantalla, producto_principal,producto_candidato, puntos, segundos):

  defaultFontGrande = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 30) # fuente grande
  defaultFont = pygame.font.Font("recursos/fonts/8-BIT WONDER.TTF", 15) # fuente normal
  textoGrande = pygame.font.Font("recursos/fonts/Pixeboy-z8XGD.ttf", 36) # fuente grande 

  background = pygame.image.load("recursos/imgs/juego_bg.jpg") # imagen de fondo (ANCHO, ALTO)
  background = pygame.transform.scale(background, (ANCHO, ALTO)) # redimensionar la imagen (ANCHO, ALTO)
  screen.blit(background, (0, 0)) # dibujar la imagen en pantalla (0,0)

  # Linea del piso
  pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70),5) # dibujar la linea (0, ALTO - 70), (ANCHO, ALTO - 70)

  ren1 = defaultFont.render(producto_candidato, 1, COLOR_TEXTO) # dibujar el texto (producto_candidato, COLOR_TEXTO)
  ren2 = defaultFont.render("Puntos * " + str(puntos), 1, COLOR_TEXTO) # dibujar el texto (puntos, COLOR_TEXTO)
  if (segundos < 15): # si el tiempo es menor a 15
    ren3 = defaultFont.render("Tiempo * " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL) # dibujar el texto (segundos, COLOR_TIEMPO_FINAL)
  else: # si el tiempo es mayor o igual a 15
    ren3 = defaultFont.render("Tiempo * " + str(int(segundos)), 1, COLOR_TEXTO) # dibujar el texto (segundos, COLOR_TEXTO)
  x_pos = 132 # posicion en x
  y_pos = ALTO - (ALTO - 125) # posicion en y (calculando la altura de la pantalla - (ALTO - 125) para que quede centrado en pantalla)  

  pos = 0 # definimos la variable de posicion
  for producto in productos_en_pantalla: # recorremos la lista de productos
    if producto[0] == producto_principal[0] and producto[1] == producto_principal[1]: # si el producto es el mismo que el principal
      nombre_en_pantalla = textoGrande.render(producto[0] + producto[1], 1, (192, 203, 220)) # definimos el producto y el tipo como nombre_en_pantalla
      screen.blit(nombre_en_pantalla, ((ANCHO / 2 - (nombre_en_pantalla.get_width() / 2), y_pos))) # dibujar nombre_en_pantalla en pantalla
      y_pos += 68 # sumamos 68 en y 
    else: # si no
      nombre_en_pantalla = str(pos) + "     " + producto[0] + producto[1] # definimos el producto y el tipo con la posicion
      screen.blit( defaultFontGrande.render(nombre_en_pantalla, 1, COLOR_LETRAS), (x_pos, y_pos)) # dibujar nombre_en_pantalla en pantalla
      y_pos += ESPACIO # sumamos ESPACIO en y
    pos += 1 # sumamos 1

  screen.blit(ren1, (190, 570)) # dibujar ren1 en pantalla coordenadas (190, 570)
  screen.blit(ren2, (440, 8)) # dibujar ren2 en pantalla coordenadas (440, 8)
  screen.blit(ren3, (10, 10)) # dibujar ren3 en pantalla coordenadas (10, 10)

#####################################################################################################
#  Funciones Puntajes
#####################################################################################################

def lectura_puntajes(): 
  archivo = open("recursos/db/puntuacion.txt", "r") # abrir el archivo
  lista = [] # crear una lista vacia
  for linea in archivo: # recorremos cada linea
    if len(linea) > 2: # si la longitud de la linea es mayor a 2
      elemento = linea.split(",") # separamos la linea por comas
      sublista = [elemento[1][:-1], int(elemento[0])] # creamos una sublista con 2 elementos
      lista.append(sublista) # agregamos la sublista a la lista
  archivo.close() # cerrar el archivo
  return lista # devolver la lista

def dibujar_puntajes(screen, lista_de_puntajes):
  botones = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 30) # fuente
  x_pos = 200 # posicion en x
  y_pos = ALTO - (ALTO - 150) # posicion en y
  pos = 1 # definimos la variable de posicion
  for puntaje in lista_de_puntajes: # recorremos la lista de puntajes
    nombre_en_pantalla = str(pos) + " - " + puntaje[0].capitalize() + " = (" + str(puntaje[1]) + ") puntos." # definimos el puntaje con la posicion 
    screen.blit(botones.render(nombre_en_pantalla, 1, (255, 255, 255)), (x_pos, y_pos)) # dibujar nombre_en_pantalla en pantalla
    pos += 1 # sumamos 1
    y_pos += 35 # sumamos 35 en y

def validarTop10(puntos): 
  puntajes = lectura_puntajes() # llamamos a la funcion lectura_puntajes
  if puntos > 0: # si puntos es mayor a 0
    if len(puntajes) <= 10: # si la longitud de puntajes es menor o igual a 10
      return True # retornamos True
    elif puntajes[9][1] < puntos: # si puntajes[9][1] es menor a puntos
      return True # retornamos True
    else: # si no 
      return False  # retornamos False

def guardarPuntajes(puntos, nombre):
  puntajes = lectura_puntajes() # llamamos a la funcion lectura_puntajes
  if [nombre, puntos] not in puntajes and puntos != 0: # si [nombre, puntos] no esta en puntajes y puntos es diferente de 0
    puntajes.append([nombre, puntos]) # agregamos [nombre, puntos] a puntajes
    puntajes.sort(key=lambda x: x[1], reverse=True) # ordenamos puntajes usando lambda x: x[1], lambda es para ordenar por el segundo elemento de la lista 
    puntajes = puntajes[:10] # cortamos puntajes a 10 
    archivo = open("recursos/db/puntuacion.txt", "w") # abrir el archivo
    for puntaje in puntajes:  # recorremos puntajes
      archivo.write(str(puntaje[1]) + "," + puntaje[0] + "\n") # escribimos puntaje[1] y puntaje[0] en el archivo
    print(puntajes) # imprimimos puntajes
    archivo.close() # cerramos el archivo

##################################################################################################
#  Funciones Fin del Juego
##################################################################################################

def cuatroLineas(texto): 
  while len(texto) <= 3: # mientras la longitud de texto sea menor o igual a 3
    texto += "_" # agregamos un guion
  return texto # retornamos texto

def dibujarFinJuego(screen, puntos, entrada, record): 
  if record: # si record es True
    background = pygame.image.load("recursos/imgs/fin_juego_bg.jpg") # cargar imagen en background
    background = pygame.transform.scale(background, (ANCHO, ALTO)) # redimensionar la imagen en background
    screen.blit(background, (0, 0))   # dibujar background en pantalla

    textoGrande = pygame.font.Font("recursos/fonts/8-BIT WONDER.TTF", 80) # fuente grande
    texto2 = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 50) # fuente chica
    texto3 = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 25) # fuente pequeña
    botones = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 30) # fuente botones

    texto_1 = textoGrande.render("SE ACABO", 1, (255, 255, 255)) # definir texto_1 con textoGrande
    texto_2 = textoGrande.render("EL TIEMPO", 1, (255, 255, 255)) # definir texto_2 con textoGrande
    texto_3 = texto2.render("Puntuacion: " + str(puntos), 1, (255, 255, 255)) # definir texto_3 con texto2
    texto_4 = texto2.render("¡Nuevo Record!", 1, (255, 255, 0)) # definir texto_4 con texto2
    texto_5 = texto3.render("(ingrese un nombre para guardar su puntuacion)", 1, (175, 175, 175)) # definir texto_5 con texto3
    boton2 = botones.render("Guardar Puntos (ENTER)", 0, 1, (255, 255, 255)) # definir boton2 con botones

    screen.blit(texto_1, (90, 30)) # dibujar texto_1 en pantalla
    screen.blit(texto_2, (60, 110)) # dibujar texto_2 en pantalla

    # parafo centralizado
    screen.blit(texto_3, (ANCHO / 2 - (texto_3.get_width() / 2), 310)) # dibujar texto_3 en pantalla usando get_width para obtener el ancho de texto_3 y ANCHO / 2 - (texto_3.get_width() / 2) para centrarlo
    screen.blit(texto_4, (ANCHO / 2 - (texto_4.get_width() / 2), 200)) # dibujar texto_4 en pantalla usando get_width para obtener el ancho de texto_4 y ANCHO / 2 - (texto_4.get_width() / 2) para centrarlo
    screen.blit(texto_5, (150, 450)) # dibujar texto_5 en pantalla
    screen.blit(boton2, (ANCHO / 2 - (boton2.get_width() / 2), 505)) # dibujar boton2 en pantalla usando get_width para obtener el ancho de boton2 y ANCHO / 2 - (boton2.get_width() / 2) para centrarlo

    nombre = texto2.render(cuatroLineas(entrada), 0, (255, 255, 255)) # definir nombre con texto2
    screen.blit(nombre, (325, 400)) # dibujar nombre en pantalla

  else: # si record es False

    background = pygame.image.load("recursos/imgs/fin_juego_bg.jpg") # cargar imagen en background
    background = pygame.transform.scale(background, (ANCHO, ALTO)) # redimensionar la imagen en background
    screen.blit(background, (0, 0))   # dibujar background en pantalla

    textoGrande = pygame.font.Font("recursos/fonts/8-BIT WONDER.TTF", 80) # fuente grande
    texto2 = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 50) # fuente chica
    botones = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 30) # fuente botones

    texto_1 = textoGrande.render("SE ACABO", 1, (255, 255, 255)) # Se dibuja el texto "SE ACABO" con textoGrande
    texto_2 = textoGrande.render("EL TIEMPO", 1, (255, 255, 255)) # Se dibuja el texto "EL TIEMPO" con textoGrande
    texto_3 = texto2.render("Puntuacion: " + str(puntos), 1, (255, 255, 255)) # Se dibuja el texto "Puntuacion: " + puntos con texto2
    boton1 = botones.render("Ir al Menu (ESC)", 0, 1, (255, 255, 255)) # Se dibuja el boton "Ir al Menu (ESC)" con botones
    boton2 = botones.render("Volver a Jugar (TAB)", 0, 1, (255, 255, 255))  # Se dibuja el boton "Volver a Jugar (TAB)" con botones

    screen.blit(texto_1, (90, 30)) # se pinta en pantalla el texto_1
    screen.blit(texto_2, (60, 110)) # se pinta en pantalla el texto_2

    screen.blit(texto_3, (ANCHO / 2 - (texto_3.get_width() / 2), 310)) # se pinta en pantalla el texto_3 usando get_width para obtener el ancho de texto_3 y ANCHO / 2 - (texto_3.get_width() / 2) para centrarlo
    
    screen.blit(boton1, (49, 505)) # se pinta en pantalla el boton1
    screen.blit(boton2, (481, 505)) # se pinta en pantalla el boton2