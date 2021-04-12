import pygame

from pygame.locals import *

import OpenGL

from OpenGL.GL import *


LARGURA_JANELA = 640
ALTURA_JANELA = 480

xBola = 0
yBola = 0

tamanhoDaBola = 20

velocidadeDaBolaEmX = 0.1

velocidadeDaBolaEmY = 0.1

yDoJogador1 = 0

yDoJogador2 = 0

TamanhoDoJogador = 20

velocidadeDoJogadorEmY = 0.1


def xDoJogador1():
    return -LARGURA_JANELA / 2 + larguraDosJogadores() / 2

def xDoJogador2():
    return LARGURA_JANELA / 2 - larguraDosJogadores() / 2

def larguraDosJogadores():
    return tamanhoDaBola

def alturaDosJogadores():
    return 3 * tamanhoDaBola

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    # Especifica as coordenadas dos vértices do retângulo, escalona e translada
    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    # Cria a janela do jogo
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # Desenha a bola e os jogadores na tela
    desenharRetangulo(xBola, yBola, tamanhoDaBola, tamanhoDaBola, 0, 0, 1)
    desenharRetangulo(xDoJogador1(), yDoJogador1, larguraDosJogadores(), alturaDosJogadores(), 1, 0, 0)
    desenharRetangulo(xDoJogador2(), yDoJogador2, larguraDosJogadores(), alturaDosJogadores(), 0, 1, 0)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

while True:
    # atualizar()
    desenhar()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.event.pump()