import pygame as py
import pygame.image
import random as rd
from audiovisual import *

###############################################
class Comida:
    def __init__(self, tam_pixel, width, height, tipo = "normal"):
        self.tam_pixel = tam_pixel
        self.width = width
        self.height = height
        self.tipos_comida = {
            "nerf": imagem_comida_nerf,
            "buff": imagem_comida_buff, 
            "normal": imagem_comida 
        }
        self.tipo = tipo  # Começa com a comida normal
        self.food_x, self.food_y = self.gerar_posicao()

    def gerar_posicao(self, snake_pixels=[]):

        food_x = round(rd.randrange(0, self.width - self.tam_pixel) / float(self.tam_pixel)) * float(self.tam_pixel)
        food_y = round(rd.randrange(0, self.height - self.tam_pixel) / float(self.tam_pixel)) * float(self.tam_pixel)

        if [food_x, food_y] not in snake_pixels:
            return food_x, food_y
        else:
            return self.gerar_posicao(snake_pixels)

    def desenhar(self, tela):
        cor = self.tipos_comida[self.tipo]
        imagem = py.transform.scale(cor, (20, 20))
        tela.blit(imagem, [self.food_x, self.food_y])
        #py.draw.rect(tela, cor, [self.food_x, self.food_y, self.tam_pixel, self.tam_pixel])

    def colisao(self, cobra):
        if cobra.x == self.food_x and cobra.y == self.food_y:
            return True
        return False
######################################################

class Cobra:
    def __init__(self, width, height):
        self.x = width / 2
        self.y = height / 2
        self.speed_x = 0
        self.speed_y = 0
        self.pixels = []

    def mover(self):# atualizar a movimentação da cobra com a velocidade nos eixos
        self.x += self.speed_x
        self.y += self.speed_y

    def virar(self, direcao, tam_pixel): #interação do jogador a partir das teclas
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

    def aumentar_tamanho(self, tam_snake): #verificamos se o tamanho da lista de pixels é igual ao tamanho que a cobra está, se estiver, deletamos o último pixel para a cobra não crescer infinitamente
        self.pixels.append([self.x, self.y])
        if len(self.pixels) > tam_snake:
            del self.pixels[0]

    def diminuir_tamanho(self):
        if len(self.pixels) > 1:
            del self.pixels[0]

    def colisao(self, width, height): # caso a cobra bata na parede
        return (
            self.x < 0 or self.x >= width
            or self.y < 0 or self.y >= height
            or [self.x, self.y] in self.pixels[:-1]
        )

    def desenhar_cobra(self, tela, cabeca_cobra):
        cabeca_cobra = cabeca_cobra
        for indice, pixel in enumerate(self.pixels):
        
            if pixel == self.pixels[-1]:  # Desenhando a cabeça
                tela.blit(cabeca_cobra, [pixel[0], pixel[1]])
            
            elif len(self.pixels) > 1 and pixel == self.pixels[0]:  # Desenhando a Cauda      
                
                if(self.pixels[indice][0] > self.pixels[indice+1][0] and self.pixels[indice][1] == self.pixels[indice+1][1]):
                    cauda = imagem_cauda_right
                elif(self.pixels[indice][0] < self.pixels[indice+1][0] and self.pixels[indice][1] == self.pixels[indice+1][1]):
                    cauda = imagem_cauda_left
                elif(self.pixels[indice][0] == self.pixels[indice+1][0] and self.pixels[indice][1] > self.pixels[indice+1][1]):
                    cauda = imagem_cauda_down
                elif(self.pixels[indice][0] == self.pixels[indice+1][0] and self.pixels[indice][1] < self.pixels[indice+1][1]):
                    cauda = imagem_cauda_up

                desenho_rabo = py.transform.scale(cauda, (20, 20))
                tela.blit(desenho_rabo, [pixel[0], pixel[1]])
                
            else:
                if(self.pixels[indice][0] > self.pixels[indice-1][0] and self.pixels[indice][1] < self.pixels[indice+1][1]) or (self.pixels[indice][1] < self.pixels[indice-1][1] and self.pixels[indice][0] > self.pixels[indice+1][0]):
                    cobra_corpo = imagem_corpo_downesq
                elif(self.pixels[indice][0] < self.pixels[indice-1][0] and self.pixels[indice][1] > self.pixels[indice+1][1]) or (self.pixels[indice][1] > self.pixels[indice-1][1] and self.pixels[indice][0] < self.pixels[indice+1][0]):
                    cobra_corpo = imagem_corpo_updir
                elif(self.pixels[indice][0] < self.pixels[indice-1][0] and self.pixels[indice][1] < self.pixels[indice+1][1]) or (self.pixels[indice][1] < self.pixels[indice-1][1] and self.pixels[indice][0] < self.pixels[indice+1][0]):
                    cobra_corpo = imagem_corpo_downdir
                elif(self.pixels[indice][0] > self.pixels[indice-1][0] and self.pixels[indice][1] > self.pixels[indice+1][1]) or (self.pixels[indice][1] > self.pixels[indice-1][1] and self.pixels[indice][0] > self.pixels[indice+1][0]):
                    cobra_corpo = imagem_corpo_upesq
                elif(self.pixels[indice][0] == self.pixels[indice-1][0]):
                    cobra_corpo = imagem_corpo_vertical
                elif(self.pixels[indice][1] == self.pixels[indice-1][1]):
                    cobra_corpo = imagem_corpo_horizontal

                desenho_corpo =  py.transform.scale(cobra_corpo, (20, 20))
                tela.blit(desenho_corpo, [pixel[0], pixel[1]])
                # py.draw.rect(screen, red, [pixel[0], pixel[1], tam_pixel, tam_pixel])
