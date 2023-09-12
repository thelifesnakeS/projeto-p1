#Atenção: estes arquivo python serve apenas para implementação de testes, o código fonte está na main.py junto com classes.py

import pygame as py
import random as rd

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


###############################################
class Comida:
    def __init__(self, tam_pixel, width, height):
        self.tam_pixel = tam_pixel
        self.width = width
        self.height = height
        self.food_x, self.food_y = self.gerar_posicao()

    def gerar_posicao(self):
        food_x = round(rd.randrange(0, self.width - self.tam_pixel) / float(self.tam_pixel)) * float(self.tam_pixel)
        food_y = round(rd.randrange(0, self.height - self.tam_pixel) / float(self.tam_pixel)) * float(self.tam_pixel)
        return food_x, food_y

    def desenhar(self, tela):
        py.draw.rect(tela, red, [self.food_x, self.food_y, self.tam_pixel, self.tam_pixel])

    def colisao(self, x, y):
        return x == self.food_x and y == self.food_y

######################################################

class Cobra:
    def __init__(self):
        self.x = width / 2
        self.y = height / 2
        self.speed_x = 0
        self.speed_y = 0
        self.pixels = []

    def mover(self):# atualizar a movimentação da cobra com a velocidade nos eixos
        self.x += self.speed_x
        self.y += self.speed_y

    def virar(self, direcao): #interação do jogador a partir das teclas
        if direcao == "up":
            self.speed_x = 0
            self.speed_y = -tam_pixel
        elif direcao == "down":
            self.speed_x = 0
            self.speed_y = tam_pixel
        elif direcao == "left":
            self.speed_x = -tam_pixel
            self.speed_y = 0
        elif direcao == "right":
            self.speed_x = tam_pixel
            self.speed_y = 0

    def aumentar_tamanho(self): #verificamos se o tamanho da lista de pixels é igual ao tamanho que a cobra está, se estiver, deletamos o último pixel para a cobra não crescer infinitamente
        self.pixels.append([self.x, self.y])
        if len(self.pixels) > tam_snake:
            del self.pixels[0]

    def colisao(self):
        return (
            self.x < 0 or self.x >= width
            or self.y < 0 or self.y >= height
            or [self.x, self.y] in self.pixels[:-1]
        )

comida = Comida(tam_pixel, width, height)
cobra = Cobra()
#food_x, food_y = gerar_food()

while not end_game:
    screen.fill(preto)

    for e in py.event.get():
        if e.type == py.QUIT:
            end_game = True
        elif e.type == py.KEYDOWN:
            if e.key == py.K_UP:
                cobra.virar("up")
            elif e.key == py.K_DOWN:
                cobra.virar("down")
            elif e.key == py.K_LEFT:
                cobra.virar("left")
            elif e.key == py.K_RIGHT:
                cobra.virar("right")

    cobra.aumentar_tamanho()
    if cobra.colisao():
        end_game = True

    cobra.mover()

    # Verifica colisão com a comida
    if cobra.x == comida.food_x and cobra.y == comida.food_y:
        tam_snake += 1
        comida.food_x, comida.food_y = comida.gerar_posicao()

    # Desenhar cobra
    for pixel in cobra.pixels:
        py.draw.rect(screen, green, [pixel[0], pixel[1], tam_pixel, tam_pixel])

    # Desenhar comida
    comida.desenhar(screen)

    # Desenhar pontuação
    fonte = py.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {tam_snake - 1}", True, yellow)
    screen.blit(texto, [1, 1])

    py.display.update()
    relogio.tick(speed)
