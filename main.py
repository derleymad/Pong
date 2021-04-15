
import sys
import pygame
from pygame.locals import *


loopdojogo = True

branco = (255,255,255)
preto = (0,0,0,0)
vermelho = (255,0,0)
verde = (0,255,0) 
azul = (0,0,255)

velocidade = [5,5] #para o modo facil
velocidadePadrao = 5

pontuacaoJogador1 = 0
pontuacaoJogador2 = 0

yJogador1 = 0
yJogador2 = 0

scale = 25

###################################################

pygame.init()


# INFORMACOES DA TELA
relogio = pygame.time.Clock()
largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))

# IMPORTA A BOLA 
bola = pygame.image.load("bola2.png")
bola = pygame.transform.scale(bola, (scale, scale))
bolarect = bola.get_rect()

class jogador():
    def __init__(self, posX, posY, largura, altura):
        self.xJogador = posX
        self.yJogador = posY
        self.largura = largura
        self.altura = altura

    def desenhaJogador(self, superficie, cor):
        pygame.draw.rect(superficie, cor, [self.xJogador, self.yJogador, self.largura, self.altura])


# DESENHA PLACAR
def placar(pontos, posX, posY, cor):
    num = str(pontos)
    fontesys = pygame.font.SysFont(None, 100)
    pontuacao = fontesys.render(num, 1, cor)
    tela.blit(pontuacao,(posX, posY))

def desenha_interface():
    pygame.draw.rect(tela, branco, [0, altura-20, largura, 20])
    pygame.draw.rect(tela, branco, [0, 0, largura, 20])
    pygame.draw.line(tela, branco, (largura/2,0), (largura/2,altura), 20)

bolarect.center = (largura/2,altura/2)

jogador1 = jogador(20, (altura/2)-40, 20, 80)
jogador2 = jogador(largura-40, (altura/2)-40, 20, 80)
jogador1Altura = (altura/2)-40

while loopdojogo:
    
    tela.fill((preto))

    #Desenha interface game

    desenha_interface()

    jogador1.desenhaJogador(tela, branco)
    jogador2.desenhaJogador(tela, branco)

    #MOVIMENTAÇÃO DA BARRA
    keys = pygame.key.get_pressed()
    if keys[K_w] and not jogador1Altura <= 20:
        jogador1.yJogador -= 5
        jogador1Altura = jogador1Altura - 5

    if keys[K_s] and not jogador1Altura >= altura-(jogador1.altura+20):
        jogador1.yJogador += 5
        jogador1Altura = jogador1Altura + 5

    '''if bolarect.left <= 40 and bolarect.top >= jogador1Altura and bolarect.bottom <= jogador1Altura + jogador1.altura:
        velocidade[0] = -velocidade[0]
    
    #if
    if bolarect.right < 40 and bolarect.bottom > jogador1Altura: 
        velocidade[1] = -velocidade[1]
    placar(jogador1Altura, 100, 100, branco)'''



    #desenhaJogador()
    #if jogador == 2: jogador2 = pygame.draw.rect(tela, branco, [largura-40, altura/2-40, 20, 80])
    #jogador1 = pygame.draw.rect(tela, branco, [20, altura/2-40, 20, 80])
    #jogador2 = pygame.draw.rect(tela, branco, [largura-40, altura/2-40, 20, 80])
    
    #PLACAR
    if pontuacaoJogador1 >= 10:
        placar(pontuacaoJogador1, largura/2-100, 30, branco)
    else:
        placar(pontuacaoJogador1, largura/2-60, 30, branco)
    placar(pontuacaoJogador2, largura/2+25, 30, branco)
    
    bolarect = bolarect.move(velocidade)


    if bolarect.left < -scale:
        pontuacaoJogador2 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade[0] = velocidadePadrao

    if bolarect.right > largura + scale:
        pontuacaoJogador1 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade[0] = -velocidadePadrao
    


    '''if bolarect.left < -scale or bolarect.right > largura+scale:
        if verifica == 1:
            velocidade[0]*-1
            verifica = 0
        else:
            velocidade[0]*1
            verifica = 1
        bolarect.center = (largura/2,altura/2)'''
        

    #if bolarect.left < 0 or bolarect.right > largura+30:
    #    bolarect.center = (largura/2,altura/2)
    #if bolarect.left < 0 or bolarect.right > largura:
    #    velocidade[0] = -velocidade[0] ## faz com que bata nas paredes
    if bolarect.top < 20 or bolarect.bottom > altura-20:
        velocidade[1] = -velocidade[1]
    tela.blit(bola,bolarect)

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loopdojogo = False
            pygame.quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                loopdojogo = False
                pygame.quit()
    
    relogio.tick(60) ## espera certos milesimos suficientes para ter 60 como fps
