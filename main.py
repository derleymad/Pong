# -*- coding: utf-8 -*-
import sys
import pygame
import Funcoes
import Bola
from Atributos import *
from Player import *

pygame.init()

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

def jogo(velocidade, numeroJogadores, dificuldade):
    tela.fill(preto)

    Funcoes.desenha_campo(branco)
    Funcoes.informacoes(numeroJogadores)
    Funcoes.desenha_jogadores()
    Funcoes.movimenta_jogadores(Bola.bolarect, numeroJogadores)
    Funcoes.colisao(Bola.bolarect, velocidade)
    Funcoes.placar()

    Bola.bolarect = Bola.bolarect.move(velocidade)

    # VERIFICA SE A BOLA SAIU, ADICIONA O PONTO E CENTRALIZA A BOLA
    if Bola.bolarect.left < -scale:
        Funcoes.jogador2.pontuacao += 1
        Bola.bolarect.center = (largura / 2, altura / 2)
        velocidade = Funcoes.define_velocidade_da_bola(dificuldade)
        velocidade[0] = velocidade[0]
        velocidade[1] = velocidade[1]

    if Bola.bolarect.right > largura + scale:
        Funcoes.jogador1.pontuacao += 1
        Bola.bolarect.center = (largura / 2, altura / 2)
        velocidade = Funcoes.define_velocidade_da_bola(dificuldade)
        velocidade[0] = -velocidade[0]
        velocidade[1] = velocidade[1]

    if Bola.bolarect.top < 20 or Bola.bolarect.bottom > altura - 20:
        velocidade[1] = -velocidade[1]
    tela.blit(Bola.bola, Bola.bolarect)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.quit()
                exit()

    pygame.display.flip()

    # ESPERA CERTOS MILÉSIMOS SUFICIENTE PARA TER 60 FPS
    relogio.tick(60)

Funcoes.introducao()
numeroJogadores = Funcoes.escolhe_numero_jogadores()
dificuldade = Funcoes.escolhe_dificuldade()
velocidade = Funcoes.define_velocidade_da_bola(dificuldade)
Funcoes.velocidade_barra_jogadores(numeroJogadores, dificuldade)

while loopdojogo:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_p:
                pause = True
                while pause:
                    escolha = Funcoes.pausa()
                    if escolha == 1:
                        pause = False
                    elif escolha == 2:
                        reinicia += 1
                        pause = False

    if Funcoes.jogador1.pontuacao == 10 or Funcoes.jogador2.pontuacao == 10:
        fimJogo = True
        while fimJogo:
            escolha = Funcoes.fim_de_jogo()
            if escolha == 1:
                reinicia += 1
                fimJogo = False

    if reinicia == 1:
        reinicia = 0
        Funcoes.jogador1.pontuacao = 0
        Funcoes.jogador2.pontuacao = 0
        Funcoes.jogador1.yJogador = alturaInicialBarra
        Funcoes.jogador2.yJogador = alturaInicialBarra
        Bola.bolarect.center = (largura / 2, altura / 2)
        numeroJogadores = Funcoes.escolhe_numero_jogadores()
        dificuldade = Funcoes.escolhe_dificuldade()
        velocidade = Bola.define_velocidade_da_bola(dificuldade)

    jogo(velocidade, numeroJogadores, dificuldade)