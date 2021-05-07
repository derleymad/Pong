# -*- coding: utf-8 -*-
import pygame
from Atributos import *

##### IMPORTANDO A BOLA  #####
bola = pygame.image.load("bola1.png")

bola = pygame.transform.scale(bola, (scale, scale))

bolarect = bola.get_rect()

bolarect.center = (largura / 2, altura / 2)

def define_velocidade_da_bola(dificuldade):
    if dificuldade == 1:
        velocidade = [velocidadeXFacilPadrao, velocidadeYFacilPadrao]
    elif dificuldade == 2:
        velocidade = [velocidadeXDificilPadrao, velocidadeYDificilPadrao]
    else:
        velocidade = 0
    return velocidade