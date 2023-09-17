import pygame as py
from classes import *

py.init()
py.display.set_caption("The Life Snake - P1")
width, height = 800, 600
screen = py.display.set_mode((width, height))
relogio = py.time.Clock()

end_game = False

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
preto = (0, 0, 0)

tam_pixel = 20
speed = 10
tam_snake = 1

comida = Comida(tam_pixel, width, height)
cobra = Cobra(width, height)

evento_anterior = ""  # Armazena a Tecla anteriormente cliclada

while not end_game:
    screen.fill(preto)

    for e in py.event.get():
        if e.type == py.QUIT:
            end_game = True

        elif e.type == py.KEYDOWN:
            if e.key == py.K_UP:
                if evento_anterior != py.K_UP and evento_anterior != py.K_DOWN:
                    cobra.virar("up", tam_pixel)
                    evento_anterior = py.K_UP

            elif e.key == py.K_DOWN:
                if evento_anterior != py.K_UP and evento_anterior != py.K_DOWN:
                    cobra.virar("down", tam_pixel)
                    evento_anterior = py.K_DOWN

            elif e.key == py.K_LEFT:
                if evento_anterior != py.K_RIGHT and evento_anterior != py.K_LEFT:
                    cobra.virar("left", tam_pixel)
                    evento_anterior = py.K_LEFT

            elif e.key == py.K_RIGHT:
                if evento_anterior != py.K_RIGHT and evento_anterior != py.K_LEFT:
                    cobra.virar("right", tam_pixel)
                    evento_anterior = py.K_RIGHT

    cobra.aumentar_tamanho(tam_snake)
    if cobra.colisao(width, height):
        end_game = True

    cobra.mover()

    # Verifica colisão com a comida
    if cobra.x == comida.food_x and cobra.y == comida.food_y:
        tam_snake += 1
        comida.food_x, comida.food_y = comida.gerar_posicao(cobra.pixels)

    # Desenhar cobra
    for pixel in cobra.pixels:
        py.draw.rect(screen, green, [pixel[0], pixel[1], tam_pixel, tam_pixel])

    # Desenhar comida
    comida.desenhar(screen, red)

    # Desenhar pontuação
    fonte = py.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {tam_snake - 1}", True, yellow)
    screen.blit(texto, [1, 1])

    py.display.update()
    relogio.tick(speed)
