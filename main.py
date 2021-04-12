import sys
import pygame
from pygame.locals import *


loopdojogo = True

branco = (255,255,255)
preto = (0,0,0,0)
vermelho = (255,0,0)
verde = (0,255,0) 
azul = (0,0,255)

velocidade = [10,10] #para o modo facil


###################################################

pygame.init()


# INFORMACOES DA TELA
relogio = pygame.time.Clock()
inf_tela = pygame.display.Info() #Da informacao de qual altura e qual largura  da tela
altura = inf_tela.current_h
largura = inf_tela.current_w

tela = pygame.display.set_mode((largura,altura))

# IMPORTA A BOLA 
bola = pygame.image.load("bola1.png")
bola = pygame.transform.scale(bola, (100, 100))
bolarect = bola.get_rect()

# DESENHA RETANGULO


#player1 = pygame.draw.rect(tela,[0,0,0],[50,50,90,90],0)

bolarect.center = (largura/2,altura/2)



#para o dificil pode ser tipo velocidade = [40,40]

while loopdojogo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            loopdojogo = False
            pygame.quit()
            
    relogio.tick(60) ## espera certos milesimos suficientes para ter 60 como fps
    tela.fill((branco))

    bolarect = bolarect.move(velocidade)

    if bolarect.left < 0 or bolarect.right > largura:
        velocidade[0] = -velocidade[0] ## faz com que bata nas paredes
    if bolarect.top < 0 or bolarect.bottom > altura:
        velocidade[1] = -velocidade[1]
    tela.blit(bola,bolarect)
    pygame.display.flip()
