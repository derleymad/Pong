import sys
import pygame
from pygame.locals import *

#Variáveis Globais
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

class jogador():
    def __init__(self, posX, posY, largura, altura, alturaInicial):
        self.xJogador = posX
        self.yJogador = posY
        self.largura = largura
        self.altura = altura
        self.alturaInicial = alturaInicial

    def desenhaJogador(self, superficie, cor):
        pygame.draw.rect(superficie, cor, [self.xJogador, self.yJogador, self.largura, self.altura])
    
    def movimentacaoBarra1(self, alturaTotal):
        keys = pygame.key.get_pressed()
        if keys[K_w] and not self.alturaInicial <= 20:
            self.yJogador -= 5
            self.alturaInicial = self.alturaInicial - 5

        if keys[K_s] and not self.alturaInicial >= alturaTotal-(self.altura+20):
            self.yJogador += 5
            self.alturaInicial = self.alturaInicial + 5
        #placar(self.alturaInicial, 100, 100, branco)
    
    def movimentacaoBarra2(self, alturaTotal):
        keys = pygame.key.get_pressed()
        if keys[K_UP] and not self.alturaInicial <= 20:
            self.yJogador -= 5
            self.alturaInicial = self.alturaInicial - 5

        if keys[K_DOWN] and not self.alturaInicial >= alturaTotal-(self.altura+20):
            self.yJogador += 5
            self.alturaInicial = self.alturaInicial + 5
        #placar(self.alturaInicial, 200, 200, branco)


def placar(pontos, posX, posY, cor):
    num = str(pontos)
    fontesys = pygame.font.SysFont(None, 100)
    pontuacao = fontesys.render(num, 1, cor)
    tela.blit(pontuacao,(posX, posY))

def desenha_interface():
    pygame.draw.rect(tela, branco, [0, altura-20, largura, 20])
    pygame.draw.rect(tela, branco, [0, 0, largura, 20])
    pygame.draw.line(tela, branco, (largura/2,0), (largura/2,altura), 20)


# IMPORTA A BOLA 
bola = pygame.image.load("bola1.png")
bola = pygame.transform.scale(bola, (scale, scale))
bolarect = bola.get_rect()

bolarect.center = (largura/2,altura/2)

alturaInicial = (altura/2)-40
jogador1 = jogador(20, (altura/2)-40, 20, 80, alturaInicial)
jogador2 = jogador(largura-40, (altura/2)-40, 20, 80, alturaInicial)

numeroJogadores = 2

while loopdojogo:
    
    tela.fill((preto))

    #Desenha interface game

    desenha_interface()

    jogador1.desenhaJogador(tela, branco)
    jogador2.desenhaJogador(tela, branco)

    if numeroJogadores == 1:
        jogador1.movimentacaoBarra1(altura)
        #movimentação barra bot
    else:
        jogador1.movimentacaoBarra1(altura)
        jogador2.movimentacaoBarra2(altura)

    '''if bolarect.left <= 40 and bolarect.top >= jogador1Altura and bolarect.bottom <= alturaInicial + jogador1.altura:
        velocidade[0] = -velocidade[0]
    
    if bolarect.right < 40 and bolarect.bottom > alturaInicial: 
        velocidade[1] = -velocidade[1]
    placar(jogador1Altura, 100, 100, branco)'''


    #PLACAR
    if pontuacaoJogador1 >= 10:
        placar(pontuacaoJogador1, largura/2-100, 30, branco)
    else:
        placar(pontuacaoJogador1, largura/2-60, 30, branco)
    placar(pontuacaoJogador2, largura/2+25, 30, branco)
    
    bolarect = bolarect.move(velocidade)


    #Verifica se a bola saiu, adiciona o ponto e centraliza a bola
    if bolarect.left < -scale:
        pontuacaoJogador2 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade[0] = velocidadePadrao

    if bolarect.right > largura + scale:
        pontuacaoJogador1 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade[0] = -velocidadePadrao    


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