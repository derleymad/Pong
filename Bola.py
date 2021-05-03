import pygame
from Atributos import scale,largura,altura

##### IMPORTANDO A BOLA  #####
bola = pygame.image.load("bola1.png")
bola = pygame.transform.scale(bola, (scale, scale))
bolarect = bola.get_rect()
bolarect.center = (largura / 2, altura / 2)
