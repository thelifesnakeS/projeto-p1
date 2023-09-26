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
branca = (255, 255, 255)

tam_pixel = 20
speed = 10
tam_snake = 1

comida_buff = Comida(tam_pixel, width, height)
comida_buff.tipo = "buff"

comida_nerf = Comida(tam_pixel, width, height)
comida_nerf.tipo = "nerf"

qtd_normal = 0
qtd_buff = 0
qtd_nerf = 0

comida = Comida(tam_pixel, width, height)
cobra = Cobra(width, height)

todas_comidas = [comida, comida_buff, comida_nerf]  #adicionar

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
   
    # Verifica borda da tela
    if cobra.x >= width:
        cobra.x = 0
    elif cobra.x < 0:
        cobra.x = width - tam_pixel
    elif cobra.y >= height:
        cobra.y = 0
    elif cobra.y < 0:
        cobra.y = height - tam_pixel


    # Verifica colisão com a comida
    for c in todas_comidas:
        if c.colisao(cobra):
            if c.tipo == 'normal':
                qtd_normal += 1
                speed *= 1.03
                tam_snake += 1

            if c.tipo == 'buff':
                qtd_buff += 1
                if tam_snake > 1:
                    tam_snake -= 1
                cobra.diminuir_tamanho()
                if speed >= 10:
                    speed *= 0.80

            if c.tipo == 'nerf':
                qtd_nerf += 1
                tam_snake += 1
                speed *= 1.10

            c.food_x, c.food_y = c.gerar_posicao()

    # Desenhar cobra
    for pixel in cobra.pixels:
        py.draw.rect(screen, green, [pixel[0], pixel[1], tam_pixel, tam_pixel])

    # Desenhar comida
    comida.desenhar(screen)

    comida_buff.desenhar(screen)
    comida_nerf.desenhar(screen)

    # Desenhar pontuação
    fonte = py.font.SysFont("Helvetica", 20)
    normal = fonte.render(f"Normal: {qtd_normal}", True, branca)
    buff = fonte.render(f"Buff: {qtd_buff}", True, yellow)
    nerf = fonte.render(f"Nerf: {qtd_nerf}", True, red)
    screen.blit(normal, [1, 1])
    screen.blit(buff, [100, 1])
    screen.blit(nerf, [200, 1])

    py.display.update()
    relogio.tick(speed)
