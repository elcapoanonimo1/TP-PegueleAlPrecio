#! /usr/bin/env python
# type: ignore
import os, sys
import pygame
from pygame.locals import *

from configuracion import *
from funciones import *
from extras import *


def puntajes():
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Peguele al precio")

    fondo = pygame.image.load("recursos/imgs/puntuaciones_bg.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    pantalla.blit(fondo, (0, 0))

    texto = pygame.font.Font("recursos/fonts/8-BIT WONDER.TTF", 55)
    texto2 = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 50)
    botones = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 30)

    texto_1 = texto.render("PUNTUACIONES", 1, (255, 255, 255))
    boton1 = botones.render("Ir al Menu (ESC)", 0, 1, (255, 255, 255))

    dibujar_puntajes(pantalla, lectura_puntajes())

    pantalla.blit(texto_1, (90, 75))
    pantalla.blit(boton1, (250, 538))

    boton1 = botones.render("Ir al Menu (ESC)", 0, 1, (255, 255, 255))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 246 <= x <= 454 and 533 <= y <= 571:
                    menu()
        pygame.display.update()


def comoJugar():
    pygame.init()
    pygame.mixer.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Peguele al precio")

    fondo = pygame.image.load("recursos/imgs/comoJugar_bg.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    pantalla.blit(fondo, (0, 0))

    texto = pygame.font.Font("recursos/fonts/8-BIT WONDER.TTF", 55)
    texto2 = pygame.font.Font("recursos/fonts/Pixeboy-z8XGD.ttf", 25)
    botones = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 30)

    texto_1 = texto.render("Como Jugar", 1, (255, 255, 255))

    linea1 = texto2.render("Al hacer clic en el boton 'Jugar', seras dirigido de inmediato", 1, (255, 255, 255))
    linea2 = texto2.render("a la pantalla de juego, donde aparecera un contador de ", 1, (255, 255, 255))
    linea3 = texto2.render("puntos y tiempo, junto con un producto principal y otros ", 1, (255, 255, 255))
    linea4 = texto2.render("adicionales, los cuales pueden ser de calidad economica o premium.", 1,(255, 255, 255))
    linea5 = texto2.render("El juego consiste en adivinar que productos podrian tener", 1, (255, 255, 255))
    linea6 = texto2.render("un precio similar al del producto principal, acumulando", 1, (255, 255, 255))
    linea7 = texto2.render("puntos en el proceso. Si seleccionas un producto con un", 1, (255, 255, 255))
    linea8 = texto2.render("precio similar al del producto principal, tus", 1, (255, 255, 255))
    linea9 = texto2.render("puntos aumentaran; de lo contrario, disminuiran.", 1, (255, 255, 255))
    linea10 = texto2.render("Una vez que el tiempo se agote, el juego finalizara,", 1, (255, 255, 255))
    linea11 = texto2.render("mostrandote los puntos obtenidos. Si tus puntos entran", 1, (255, 255, 255))
    linea12 = texto2.render("en el ranking de los 10 mejores podras ingresar", 1, (255, 255, 255))
    linea13 = texto2.render("un nombre (de 4 digitos) para guardarlo.", 1, (255, 255, 255))
    boton1 = botones.render("Ir al Menu (ESC)", 0, 1, (255, 255, 255))

    pantalla.blit(texto_1, (120, 10))
    pantalla.blit(linea1, (70, 90))
    pantalla.blit(linea2, (70, 130))
    pantalla.blit(linea3, (70, 170))
    pantalla.blit(linea4, (70, 210))
    pantalla.blit(linea5, (70, 250))
    pantalla.blit(linea6, (70, 290))
    pantalla.blit(linea7, (70, 330))
    pantalla.blit(linea8, (70, 370))
    pantalla.blit(linea9, (70, 410))
    pantalla.blit(linea10, (70, 450))
    pantalla.blit(linea11, (70, 480))
    pantalla.blit(linea12, (70, 510))
    pantalla.blit(linea13, (70, 530))
    pantalla.blit(boton1, (260, 560))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 257 <= x <= 460 and 557 <= y <= 583:
                    menu()
        pygame.display.update()

def finDelJuego(puntos):
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load("recursos/sfx/juego_terminado0.mp3")
    pygame.mixer.music.play()

    if validarTop10(puntos):
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Peguele al precio")

        inputNombre = ""
        dibujarFinJuego(pantalla, puntos, inputNombre, True)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu()

                elif event.type == pygame.KEYDOWN and event.key in range(pygame.K_a, pygame.K_z + 1):
                    if len(inputNombre) < 4:
                        inputNombre += pygame.key.name(event.key)
                        dibujarFinJuego(pantalla, puntos, inputNombre, True)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    inputNombre = inputNombre[0 : len(inputNombre) - 1]
                    dibujarFinJuego(pantalla, puntos, inputNombre, True)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if inputNombre == "":
                        guardarPuntajes(puntos, "XXXX")
                    else:
                        guardarPuntajes(puntos, inputNombre)
                    puntajes()
                    pygame.mixer.init()
                    pygame.mixer.music.load("recursos/music/music.mp3")
                    pygame.mixer.music.play(99)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 249 <= x <= 553 and 504 <= y <= 532:
                        if inputNombre == "":
                            guardarPuntajes(puntos, "XXXX")
                        else:
                            guardarPuntajes(puntos, inputNombre)
                        puntajes()
            pygame.display.update()

    else:
        pygame.init()
        pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load("recursos/sfx/juego_terminado1.mp3")
        pygame.mixer.music.play()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Peguele al precio")

        inputNombre = ""
        dibujarFinJuego(pantalla, puntos, inputNombre, False)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    menu()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                    jugar()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if 48 <= x <= 249 and 502 <= y <= 533:
                        menu()
                    elif 476 <= x <= 765 and 497 <= y <= 543:
                        jugar()
            pygame.display.update()
        pygame.display.flip()


def jugar():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()
    mjuego = pygame.mixer.music.load("recursos/music/juego.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    pantalla = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    # totaltime = 0
    totaltime = pygame.time.get_ticks()  # Inicializar el tiempo total
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    # Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
    # print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(pantalla, productos_en_pantalla, producto, producto_candidato, puntos, segundos)

    while segundos > fps / 1000:
        # 1 frame cada 1/fps segundos
        # gameClock.tick(fps)
        # totaltime += gameClock.get_time()
        gameClock.tick(fps)
        current_time = pygame.time.get_ticks()  # Obtener el tiempo actual
        elapsed_time = current_time - totaltime  # Calcular el tiempo transcurrido
        totaltime = current_time  # Actualizar el tiempo total

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():
            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                menu()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[
                        0 : len(producto_candidato) - 1
                    ]

                if producto_candidato.isnumeric():
                    if int(producto_candidato) > 6 or int(producto_candidato) < 1:
                        pygame.mixer.Sound("recursos/sfx/error.mp3").play()
                else:
                    pygame.mixer.Sound("recursos/sfx/error.mp3").play()

                if e.key == K_RETURN:  # presionó enter
                    indice = (int(producto_candidato) if producto_candidato.isnumeric() else 0)

                    # chequeamos si el producto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla) and indice != 0:
                        proceso = procesar(producto, productos_en_pantalla[indice], MARGEN)

                        if proceso > 0:
                            pygame.mixer.Sound("recursos/sfx/bien.mp3").play()
                        # pygame.mixer.music.play(0)
                        elif proceso <= 0:
                            pygame.mixer.Sound("recursos/sfx/mal.mp3").play()
                        # pygame.mixer.music.play(0)

                        if proceso:
                            puntos += proceso
                            if puntos < 0:
                                puntos = 0
                        elif puntos == 0 and proceso < 0:
                            return 0

                        producto_candidato = ""
                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 118 <= x <= 683 and 190 <= y <= 226:
                    indice = 1
                elif 118 <= x <= 683 and 238 <= y <= 277:
                    indice = 2
                elif 118 <= x <= 683 and 290 <= y <= 327:
                    indice = 3
                elif 118 <= x <= 683 and 340 <= y <= 378:
                    indice = 4
                elif 118 <= x <= 683 and 392 <= y <= 429:
                    indice = 5
                elif 118 <= x <= 683 and 440 <= y <= 479:
                    indice = 6
                else:
                    indice = 0

                if indice < len(productos_en_pantalla) and indice != 0:
                    proceso = procesar(producto, productos_en_pantalla[indice], MARGEN)

                    if proceso > 0:
                        pygame.mixer.Sound("recursos/sfx/bien.mp3").play()
                        # pygame.mixer.music.play(0)
                    elif proceso <= 0:
                        pygame.mixer.Sound("recursos/sfx/mal.mp3").play()
                        # pygame.mixer.music.play(0)

                    if proceso:
                        puntos += proceso
                        if puntos < 0:
                            puntos = 0
                    elif puntos == 0 and proceso < 0:
                        return 0

                    producto_candidato = ""
                    # Elegir un producto
                    producto = dameProducto(lista_productos, MARGEN)
                    # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                    productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
                else:
                    producto_candidato = ""

        # segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
        segundos -= (elapsed_time / 1000)  # Restar el tiempo transcurrido al tiempo restante
        # Limpiar pantalla anterior
        pantalla.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(pantalla,
            productos_en_pantalla,
            producto,
            producto_candidato,
            puntos,
            segundos,)

        pygame.display.flip()

    if segundos <= fps / 1000:
        finDelJuego(puntos)

    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                menu()
                return 0


def menu():
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("recursos/music/music.mp3")
    pygame.mixer.music.play(99)
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Peguele al precio")

    fondo = pygame.image.load("recursos/imgs/menu_bg.png")
    fondo = pygame.transform.scale(fondo, (900, 900))
    pantalla.blit(fondo, (0, 0))

    def render_con_fondo(font, text, color, border_color, border_size):
        # Renderizar el texto principal
        texto_trabajar = font.render(text, True, color)

        # Crear una superficie para el texto con borde
        borde_trabajado = pygame.Surface(texto_trabajar.get_size())

        # Dibujar el texto principal en la superficie del borde con un desplazamiento
        borde_trabajado.blit(texto_trabajar, (border_size, border_size))

        # Dibujar el texto principal en la posición original

        return borde_trabajado

    font = pygame.font.Font("recursos/fonts/Arcadepix Plus.ttf", 36)

    jugar_text = render_con_fondo(font, "Jugar", (255, 255, 255), (0, 0, 0), 0)
    info_text = render_con_fondo(font, "Como Jugar", (255, 255, 255), (0, 0, 0), 0)
    puntajes_text = render_con_fondo(
        font, "Puntuaciones", (255, 255, 255), (0, 0, 0), 0)
    salir_text = render_con_fondo(font, "Salir", (255, 255, 255), (0, 0, 0), 0)

    # coloca una imagen
    image = pygame.image.load("recursos/imgs/Logo.png")
    # achica la imagen
    image = pygame.transform.scale(image, (700, 250))
    pantalla.blit(image, (80, 20))
    # define el tamaño de la imagen

    pantalla.blit(jugar_text, (358, 310))
    pantalla.blit(info_text, (320, 360))
    pantalla.blit(puntajes_text, (310, 410))
    pantalla.blit(salir_text, (360, 460))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # print(x,y)
                if 350 <= x <= 446 and 315 <= y <= 343:
                    pygame.mixer.Sound("recursos/sfx/play.mp3").play()
                    jugar()
                elif 350 <= x <= 532 and 362 <= y <= 386:
                    comoJugar()
                elif 350 <= x <= 560 and 417 <= y <= 438:
                    puntajes()
                elif 350 <= x <= 434 and 459 <= y <= 491:
                    running = False
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu()
