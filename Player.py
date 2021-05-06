# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from Atributos import *

class Jogador():
    def __init__(self, posicaoX, posicaoY, larguraJogador, alturaJogador, pontuacao, velocidade):
        self.xJogador = posicaoX
        self.yJogador = posicaoY
        self.largura = larguraJogador
        self.altura = alturaJogador
        self.pontuacao = pontuacao
        self.velocidade = velocidade

    def desenha_jogador(self, superficie, cor):
        pygame.draw.rect(superficie, cor, [self.xJogador, self.yJogador, self.largura, self.altura])

    def movimentacao_barra_1(self, alturaTotal):
        keys = pygame.key.get_pressed()

        if keys[K_w] and not self.yJogador <= 20:
            self.yJogador -= self.velocidade

        if keys[K_s] and not self.yJogador >= alturaTotal - (self.altura + 20):
            self.yJogador += self.velocidade

    def movimentacao_barra_2(self, alturaTotal):
        keys = pygame.key.get_pressed()
        if keys[K_i] and not self.yJogador <= 20:
            self.yJogador -= self.velocidade

        if keys[K_j] and not self.yJogador >= alturaTotal - (self.altura + 20):
            self.yJogador += self.velocidade

    def movimentacao_barra_bot(self, bola, alturaTotal, larguraTotal):
        if bola.top < self.yJogador and not self.yJogador <= 20:
            self.yJogador -= self.velocidade
        elif bola.bottom > self.yJogador + 80 and not self.yJogador >= alturaTotal - (self.altura + 20):
            self.yJogador += self.velocidade