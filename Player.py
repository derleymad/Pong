import pygame
from pygame.locals import *
from Atributos import *

class jogador():
    def __init__(self, posicaoX, posicaoY, larguraJogador, alturaJogador, pontuacao, velocidade):
        self.xJogador = posicaoX
        self.yJogador = posicaoY
        self.largura = larguraJogador
        self.altura = alturaJogador
        self.pontuacao = pontuacao
        self.velocidade = velocidade

    def desenhaJogador(self, superficie, cor):
        pygame.draw.rect(superficie, cor, [self.xJogador, self.yJogador, self.largura, self.altura])

    def movimentacaoBarra1(self, alturaTotal, velocidade):
        keys = pygame.key.get_pressed()

        if keys[K_w] and not self.yJogador <= 20:
            self.yJogador -= velocidade

        if keys[K_s] and not self.yJogador >= alturaTotal - (self.altura + 20):
            self.yJogador += velocidade

    def movimentacaoBarra2(self, alturaTotal, velocidade):
        keys = pygame.key.get_pressed()
        if keys[K_i] and not self.yJogador <= 20:
            self.yJogador -= velocidade

        if keys[K_j] and not self.yJogador >= alturaTotal - (self.altura + 20):
            self.yJogador += velocidade

    def movimentacaoBarraBot(self, bola, alturaTotal, larguraTotal, velocidade):
        if bola.top < self.yJogador and not self.yJogador <= 20:
            self.yJogador -= velocidade
        elif bola.bottom > self.yJogador + 80 and not self.yJogador >= alturaTotal - (self.altura + 20):
            self.yJogador += velocidade

jogador1 = jogador(0, alturaInicialBarra, larguraJogadores, alturaJogadores, 0, 5)
jogador2 = jogador(largura - (larguraJogadores), alturaInicialBarra, larguraJogadores, alturaJogadores, 0, 5)
