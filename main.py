import pygame as py
import pygame.image
from audiovisual import *
from classes import *

py.init()
py.display.set_caption("The Life Snake - P1")
width, height = 800, 600
screen = py.display.set_mode((width, height))
relogio = py.time.Clock()

end_game = False

on = True

def jogo(end_game):
    tam_pixel = 20
    speed = 10
    tam_snake = 1

    comida_buff = Comida(tam_pixel, width, height, "buff")


    qtd_normal = 0
    qtd_buff = 0
    qtd_nerf = 0

    #comida = Comida(tam_pixel, width, height)
    cobra = Cobra(width, height)

    todas_comidas = [comida_buff]  #adicionar

    for i in range (10):
        todas_comidas.append(Comida(tam_pixel, width, height))

    for i in range (10):
        todas_comidas.append(Comida(tam_pixel, width, height, "nerf"))

    evento_anterior = ""  # Armazena a Tecla anteriormente cliclada
    cabeca = imagem_cabeca_up
    cabeca_cobra = py.transform.scale(cabeca, (20, 20))
    while not end_game:
        global on
        screen.blit(new_background, [0, 0])

        for e in py.event.get():
            if e.type == py.QUIT:
                end_game = True
                on = False

            elif e.type == py.KEYDOWN:
                if e.key == py.K_UP:
                    if evento_anterior != py.K_UP and evento_anterior != py.K_DOWN:
                        cobra.virar("up", tam_pixel)
                        evento_anterior = py.K_UP
                        cabeca = imagem_cabeca_up

                elif e.key == py.K_DOWN:
                    if evento_anterior != py.K_UP and evento_anterior != py.K_DOWN:
                        cobra.virar("down", tam_pixel)
                        evento_anterior = py.K_DOWN
                        cabeca = imagem_cabeca_down

                elif e.key == py.K_LEFT:
                    if evento_anterior != py.K_RIGHT and evento_anterior != py.K_LEFT:
                        cobra.virar("left", tam_pixel)
                        evento_anterior = py.K_LEFT
                        cabeca = imagem_cabeca_left

                elif e.key == py.K_RIGHT:
                    if evento_anterior != py.K_RIGHT and evento_anterior != py.K_LEFT:
                        cobra.virar("right", tam_pixel)
                        evento_anterior = py.K_RIGHT
                        cabeca = imagem_cabeca_right
        
        cabeca_cobra = py.transform.scale(cabeca, (20, 20))

        cobra.aumentar_tamanho(tam_snake)
        if cobra.colisao(width, height):
            game_over(screen, width, qtd_normal, qtd_buff, qtd_nerf)
            end_game = True

        cobra.mover()
    
        # Verifica colisão com a comida
        for c in todas_comidas:

            if c.colisao(cobra):
                if c.tipo == 'normal':
                    qtd_normal += 1
                    speed *= 1.03
                    tam_snake += 1
                    som_comida.play()

                if c.tipo == 'buff':
                    qtd_buff += 1
                    if tam_snake > 1:
                        tam_snake -= 1
                        som_comida.play()
                    cobra.diminuir_tamanho()
                    if speed >= 10:
                        speed *= 0.80

                if c.tipo == 'nerf':
                    qtd_nerf += 1
                    tam_snake += 1
                    speed *= 1.10
                    som_comida.play()

                c.food_x, c.food_y = c.gerar_posicao(cobra.pixels)

        # Desenhar cobra
        cobra.desenhar_cobra(screen, cabeca_cobra)

        # Verifica borda da tela
        if cobra.x >= width:
            cobra.x = 0
        elif cobra.x < 0:
            cobra.x = width - tam_pixel
        elif cobra.y >= height:
            cobra.y = 0
        elif cobra.y < 0:
            cobra.y = height - tam_pixel

        # Desenhar comida
        #comida.desenhar(screen)
        comida_buff.desenhar(screen)
        #comida_nerf.desenhar(screen)
        for c in todas_comidas[1:]:
            c.desenhar(screen)

        # Desenhar pontuação
        fonte = py.font.SysFont("Helvetica", 20)
        normal = fonte.render(f"Normal: {qtd_normal}", True, red)
        buff = fonte.render(f"Buff: {qtd_buff}", True, yellow)
        nerf = fonte.render(f"Nerf: {qtd_nerf}", True, preto)
        screen.blit(normal, [1, 1])
        screen.blit(buff, [100, 1])
        screen.blit(nerf, [200, 1])

        py.display.update()
        relogio.tick(speed)

        if on == True:
            def game_over(screen, width, normal, buff, nerf):
                global on
                jogar = True
                while jogar:
                    screen.blit(background, [0, 0])
                    fonte1 = py.font.SysFont("Helvetica", 80)
                    fonte = py.font.SysFont("Helvetica", 30)
                    fonte2 = py.font.SysFont("Helvetica", 40)
                    texto_game_over = fonte1.render("Game Over >:)", True, red)
                    pontos_normais = fonte.render(f"Pontos Normais: {normal} x 1", True, red)
                    pontos_buff = fonte.render(f"Pontos Buff: {buff} x 0", True, yellow)
                    pontos_nerf = fonte.render(f"Pontos Nerff: {nerf} x 2", True, preto)
                    total = int(normal + (nerf * 2))
                    pontos_totais = fonte2.render(f"Pontos Totais: {total}", True, blue)
                    reiniciar = fonte.render("Press R to Restart", True, branca)
                    sair = fonte.render("Press Q to Quit", True, branca)
                        
                    screen.blit(texto_game_over, (width / 2 - texto_game_over.get_width() / 2, 60))
                    screen.blit(pontos_normais, (width / 2 - pontos_normais.get_width() / 2, 200))
                    screen.blit(pontos_buff, (width / 2 - pontos_buff.get_width() / 2, 240))
                    screen.blit(pontos_nerf, (width / 2 - pontos_nerf.get_width() / 2, 280))
                    screen.blit(pontos_totais, (width / 2 - pontos_totais.get_width() / 2, 320))
                    screen.blit(reiniciar, (100, 410))
                    screen.blit(sair,(500, 410))
                        

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            on = False
                            jogar = False
                            
                                
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                on = True
                                jogar = False
                            elif event.key == pygame.K_q:
                                on = False
                                jogar = False

                        py.display.update()
    
while on:
    jogo(end_game)
    