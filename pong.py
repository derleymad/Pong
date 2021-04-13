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

def atualizar():
    global xBola, yBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoJogador1, yDoJogador2, velocidadeDoJogadorEmY, TamanhoDoJogador

    xBola = xBola + velocidadeDaBolaEmX
    yBola = yBola + velocidadeDaBolaEmY

    # Verifica se o jogador 2 rebateu a bola
    if (xBola + tamanhoDaBola / 2 > xDoJogador2() - larguraDosJogadores() / 2
    and yBola - tamanhoDaBola / 2 < yDoJogador2 + alturaDosJogadores() / 2
    and yBola + tamanhoDaBola / 2 > yDoJogador2 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    # Verifica se o jogador 1 rebateu a bola
    if (xBola - tamanhoDaBola / 2 < xDoJogador1() + larguraDosJogadores() / 2
    and yBola - tamanhoDaBola / 2 < yDoJogador1 + alturaDosJogadores() / 2
    and yBola + tamanhoDaBola / 2 > yDoJogador1 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    # Atualiza o movimento da bola ao ser rebatida pelo jogador 2
    if yBola + tamanhoDaBola / 2 > ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    # Atualiza o movimento da bola ao ser rebatida pelo jogador 1
    if yBola - tamanhoDaBola / 2 < -ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    # Verifica se um ponto foi marcado e centraliza a bola
    if xBola < -LARGURA_JANELA / 2 or xBola > LARGURA_JANELA / 2:
        xBola = 0
        yBola = 0

    keys = pygame.key.get_pressed()

    if(xBola > LARGURA_JANELA / 5):
        if(yBola > yDoJogador2  and not (yDoJogador2 + TamanhoDoJogador > ALTURA_JANELA / 2)):
            yDoJogador2 += velocidadeDoJogadorEmY

        elif(yBola < yDoJogador2 and not (yDoJogador2 - TamanhoDoJogador < - ALTURA_JANELA / 2)):
            yDoJogador2 -= velocidadeDoJogadorEmY

    # if yDoJogador2 + TamanhoDoJogador > ALTURA_JANELA / 2:
    #     velocidadeDoJogadorEmY = -velocidadeDoJogadorEmY

    # if yDoJogador2 - TamanhoDoJogador < -ALTURA_JANELA / 2:
    #     velocidadeDoJogadorEmY = -velocidadeDoJogadorEmY

    # Verifica se a tecla "w" foi apertada e sobe o jogador 1
    if(keys[K_w] and not (yDoJogador1 + TamanhoDoJogador > ALTURA_JANELA / 2)):
        yDoJogador1 = yDoJogador1 + 0.3

    #Verifica se a tecla "s" foi apertada e desce o jogador 1
    if(keys[K_s] and not (yDoJogador1 - TamanhoDoJogador < - ALTURA_JANELA / 2)):
        yDoJogador1 = yDoJogador1 - 0.3

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
    atualizar()
    desenhar()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.event.pump()
