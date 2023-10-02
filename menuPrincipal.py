import pygame
import sys
import audiovisual

pygame.init()

# Definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da janela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Seu Jogo")


# Função para desenhar texto na tela
def draw_text(text, font, color, surface, x, y):

    # Formatação de texto
    text_surface = font.render(text, True, color)
    text_width = text_surface.get_width()

    # Ajuste a posição x para centralizar o texto na tela
    x = (surface.get_width() - text_width) // 2

    # Renderize o texto na posição x calculada e na posição y fornecida
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Loop do menu
def main_menu():
    booleano_menu = True
    while booleano_menu:
        new_background = audiovisual.background
        screen.blit(new_background, [0, 0])
        draw_text('The Life Snake', pygame.font.SysFont('snapitc', 70), WHITE, screen, 250, 150)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Botão "Iniciar"
        button_start = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, WHITE, button_start)
        draw_text('Iniciar', pygame.font.Font(None, 36), BLACK, screen, 350, 310)

        # Botão "Sair"
        button_quit = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(screen, WHITE, button_quit)
        draw_text('Sair', pygame.font.Font(None, 36), BLACK, screen, 370, 410)

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint((mouse_x, mouse_y)):
                    # Iniciar o jogo aqui
                    booleano_menu = False
                    pass
                if button_quit.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


