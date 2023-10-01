import pygame as py
import pygame.image

#  Definição de Cores
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
preto = (0, 0, 0)
branca = (255, 255, 255)
blue = (105,89,205)

# Definindo Backgroud
background = py.image.load("./imagens/meu_xadrez.png")
new_background = py.transform.scale(background, (800, 600))

# Definindo imagens

imagem_comida = py.image.load("./imagens/apple.png")
imagem_comida_nerf = py.image.load("./imagens/nerf_maca.png")
imagem_comida_buff = py.image.load("./imagens/buff_macadourada.png")

imagem_cabeca_up = py.image.load("./imagens/head_up.png")
imagem_cabeca_down = py.image.load("./imagens/head_down.png")
imagem_cabeca_right= py.image.load("./imagens/head_right.png")
imagem_cabeca_left = py.image.load("./imagens/head_left.png")

imagem_cauda_up = pygame.image.load("./imagens/cauda_up.png")
imagem_cauda_down = py.image.load("./imagens/cauda_down.png")
imagem_cauda_right = py.image.load("./imagens/cauda_right.png")
imagem_cauda_left = py.image.load("./imagens/cauda_left.png")

imagem_corpo_updir = py.image.load('./imagens/body_topright.png')
imagem_corpo_upesq = py.image.load('./imagens/body_topleft.png')
imagem_corpo_downdir = py.image.load('./imagens/body_bottomright.png')
imagem_corpo_downesq = py.image.load('./imagens/body_bottomleft.png')
imagem_corpo_vertical = py.image.load('./imagens/body_vertical.png')
imagem_corpo_horizontal = py.image.load('./imagens/body_horizontal.png')

#Sons
pygame.init()
som_comida = pygame.mixer.Sound('./sound/som_comida.wav')






