import sys
import pygame
from pygame.locals import *

##### INFORMAÇÕES DA TELA #####
pygame.init()
relogio = pygame.time.Clock()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))

###### VARIÁVEIS GLOBAIS #####
loopdojogo = True
numeroJogadores = 1
G = 20
tam = 100

branco = (255,255,255)
preto = (0,0,0,0)
vermelho = (255,0,0)
verde = (0,255,0) 
azul = (0,0,255)
cores = (vermelho, azul, verde, preto)

velocidadeXFacilPadrao = 5
velocidadeYFacilPadrao = 5
velocidade = [velocidadeXFacilPadrao, velocidadeYFacilPadrao] # PARA O MODO FÁCIL
velocidadePadrao = 5

pontuacaoJogador1 = 0
pontuacaoJogador2 = 0

yJogador1 = 0
yJogador2 = 0

alturaJogadores = 80
larguraJogadores = 20

scale = 25

alturaInicialBarra = (altura/2)-(alturaJogadores/2)

##### IMPORTANDO A BOLA  #####
bola = pygame.image.load("bola1.png")
bola = pygame.transform.scale(bola, (scale, scale))
bolarect = bola.get_rect()
bolarect.center = (largura/2,altura/2)

##### CLASSES #####
class jogador():
    def __init__(self, posicaoX, posicaoY, larguraJogador, alturaJogador):
        self.xJogador = posicaoX
        self.yJogador = posicaoY
        self.largura = larguraJogador
        self.altura = alturaJogador
        self.posicaoAnterior = posicaoY

    def desenhaJogador(self, superficie, cor):
        pygame.draw.rect(superficie, cor, [self.xJogador, self.yJogador, self.largura, self.altura])
    
    def movimentacaoBarra1(self, alturaTotal, velocidade):
        keys = pygame.key.get_pressed()

        if keys[K_w] and not self.yJogador <= 20:
            self.posicaoAnterior = self.yJogador
            self.yJogador -= velocidade

        if keys[K_s] and not self.yJogador >= alturaTotal-(self.altura+20):
            self.posicaoAnterior = self.yJogador
            self.yJogador += velocidade

        #pontos(self.yJogador, 100, 100, branco)
        #pontos(self.posicaoAnterior, 100, 200, branco)
        #pontos(self.xJogador+self.largura, 200, 200, branco)
    
    def movimentacaoBarra2(self, alturaTotal, velocidade):
        keys = pygame.key.get_pressed()

        if keys[K_UP] and not self.yJogador <= 20:
            self.posicaoAnterior = self.yJogador
            self.yJogador -= velocidade

        if keys[K_DOWN] and not self.yJogador >= alturaTotal-(self.altura+20):
            self.posicaoAnterior = self.yJogador
            self.yJogador += velocidade

        #pontos(self.yJogador, 200, 200, branco)
    
    def movimentacaoBarraBot(self, bola, alturaTotal, larguraTotal, velocidade):
        if bola.top < self.yJogador and not self.yJogador <= 20:
            self.posicaoAnterior = self.yJogador
            self.yJogador -= velocidade
        elif bola.bottom > self.yJogador + 80 and not self.yJogador >= alturaTotal-(self.altura+20):
            self.posicaoAnterior = self.yJogador
            self.yJogador += velocidade

        #pontos(self.yJogador, 200, 200, branco)

##### FUNÇÕES #####
def pontos(pontos, posX, posY, cor):
    num = str(pontos)
    fontesys = pygame.font.SysFont(None, 100)
    pontuacao = fontesys.render(num, 1, cor)
    tela.blit(pontuacao,(posX, posY))

def desenha_campo():
    pygame.draw.rect(tela, branco, [0, altura-20, largura, 20])
    pygame.draw.rect(tela, branco, [0, 0, largura, 20])
    pygame.draw.line(tela, branco, (largura/2,0), (largura/2,altura), 20)

def desenha_jogadores():
    jogador1.desenhaJogador(tela, branco)
    jogador2.desenhaJogador(tela, branco)

def movimenta_jogadores():
    if numeroJogadores == 1:
        jogador1.movimentacaoBarra1(altura, velocidadePadrao)
        jogador2.movimentacaoBarraBot(bolarect ,altura, largura, velocidadePadrao)
    else:
        jogador1.movimentacaoBarra1(altura, velocidadePadrao)
        jogador2.movimentacaoBarra2(altura, velocidadePadrao)

def colisao():
    if bolarect.bottom > jogador1.yJogador and bolarect.top < jogador1.yJogador + jogador1.altura:
        if velocidade[0] < 0 and bolarect.left < jogador1.xJogador+jogador1.largura:
            velocidade[0] = -velocidade[0]
    
    if bolarect.bottom > jogador2.yJogador and bolarect.top < jogador2.yJogador + jogador2.altura:
        if velocidade[0] > 0 and bolarect.right > jogador2.xJogador:
            velocidade[0] = -velocidade[0]
    
    '''if bolarect.left < jogador1.xJogador + jogador1.largura and jogador1.yJogador < bolarect.bottom and jogador1.yJogador + jogador1.altura > bolarect.top and bolarect.right > jogador1.xJogador + (jogador1.largura/2):

    if bolarect.right > jogador2.xJogador and jogador2.yJogador < bolarect.bottom and jogador2.yJogador + jogador2.altura > bolarect.top and bolarect.left < largura - (jogador2.largura/2):'''

def placar():
    if pontuacaoJogador1 >= 10:
        pontos(pontuacaoJogador1, largura/2-100, 30, branco)
    else:
        pontos(pontuacaoJogador1, largura/2-60, 30, branco)
    pontos(pontuacaoJogador2, largura/2+25, 30, branco)

def aux_intro(pontos, posX, posY, cor, tam):
    num = str(pontos)
    fontesys = pygame.font.SysFont(None, tam)
    pontuacao = fontesys.render(num, 1, cor)
    tela.blit(pontuacao, (posX, posY))

def pausa():
    pygame.draw.rect(tela, branco, [(largura/2)-50, (altura/2)-50, 300, 300])

def jogo():
    global pontuacaoJogador1, pontuacaoJogador2, bolarect
    pause = True
    
    tela.fill((preto))

    desenha_campo()
    desenha_jogadores()
    movimenta_jogadores()
    colisao()
    placar()
    
    keys = pygame.key.get_pressed()
    bolarect = bolarect.move(velocidade)

    # VERIFICA SE A BOLA SAIU, ADICIONA O PONTO E CENTRALIZA A BOLA
    if bolarect.left < -scale:
        pontuacaoJogador2 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade[0] = velocidadeXFacilPadrao
        velocidade[1] = velocidadeYFacilPadrao

    if bolarect.right > largura + scale:
        pontuacaoJogador1 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade[0] = -velocidadeXFacilPadrao
        velocidade[1] = velocidadeYFacilPadrao

    if bolarect.top < 20 or bolarect.bottom > altura-20:
        velocidade[1] = -velocidade[1]
    tela.blit(bola,bolarect)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loopdojogo = False
            pygame.quit()
            exit()

    if keys[K_ESCAPE]:
        loop = False
        pygame.quit()
        exit()
    '''if keys[K_p]:
        pausa()
        loop = False'''

    pygame.display.flip()

    relogio.tick(60) ## espera certos milesimos suficientes para ter 60 como fps

def introducao():
    global preto, branco, cores, altura, velocidade, G, relogio

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loopdojogo = False
            pygame.quit()

    tela.fill(preto)
    pygame.time.delay(1000)
    for i in range(50):
        tela.fill(preto)
        aux_intro("Uma produção de:", 250, 250, branco, i)
        aux_intro("Equipe 4", 0 + (i * 6.6), 300, branco, 50)
        pygame.display.update()
        relogio.tick(100)

    pygame.time.delay(2000)

    tela.fill(preto)

    aux_intro("P o", 310, 250, branco, tam)
    aux_intro("ng", 430, 250, branco, tam)
    pygame.display.update()
    pygame.time.delay(2000)

    clock = pygame.time.Clock()

    comeca = True

    acc_y = 0
    acc_x = 0
    pos = [largura / 2, altura / 2]

    while comeca:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                comeca = False
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                comeca = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                acc_y = -10
                clock = pygame.time.Clock()

        t = clock.get_time() / 1000
        F = G * t
        acc_y += F

        if pos[1] > 400:
            acc_y = -10
            clock = pygame.time.Clock()
        elif pos[1] < 0:
            acc_y = 10
            clock = pygame.time.Clock()

        pos[1] += acc_y
        tela.fill(preto)
        aux_intro("P", 310, 250, branco, tam)
        aux_intro("ng", 430, 250, branco, tam)
        pygame.draw.circle(tela, branco, (pos[0], pos[1]), 20, 10)

        tempo = int(pygame.time.get_ticks() / 1000)

        if tempo > 4:
            if tempo % 2 == 0:
                aux_intro("[Aperte qualquer tecla para continuar]", largura / 3.7, altura / 1.4, branco, 30)
        pygame.display.update()
        clock.tick(60)

jogador1 = jogador(0, alturaInicialBarra, larguraJogadores, alturaJogadores)
jogador2 = jogador(largura-(larguraJogadores), alturaInicialBarra, larguraJogadores, alturaJogadores)

introducao()
while loopdojogo:
    jogo()
