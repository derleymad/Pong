import sys
import pygame
from pygame.locals import *


pygame.init()

tela = pygame.display.set_mod((640,480))

bola = pygame.image.load("bola1.png")
bola = pygame.tranform.scale(bola(100,100))
bolarect = bola.get_rect()
relogio = pygame.time.Clock()
loopdojogo = True

player1 = pygame.draw.rect(tela,[0,0,0],[50,50,90,90],0)

largura = tela.get_width()
altura = tela.get_height()

bolarect.center = (largura/2,altura/2)

#para o modo facil
velocidade = [10,10]

#para o dificil pode ser tipo velocidade = [40,40]

while loopdojogo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            loopdojogo = False
            pygame.quit()
    relogio.tick(60) ## espera certos milesimos suficientes para ter 60 como fps
    tela.fill((100,100,100))

    bolarect = bolarect.move(velocidade)

    if bolarect.left < 0 or bolarect.right > largura:
        velocidade[0] = -speed[0] ## faz com que bata nas paredes
    if bolarect.left < 0 or bolarect.right > altura:
        velocidade[1] = -speed[1]
    tela.blit(bola,bolarect)
    pygame.display.flip()
    

