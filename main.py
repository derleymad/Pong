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
G = 20
tam = 100

branco = (255,255,255)
preto = (0,0,0,0)
vermelho = (255,0,0)
verde = (0,255,0) 
azul = (0,0,255)
cinza = (25,25,25)
cores = (vermelho, azul, verde, preto)

velocidadeXFacilPadrao = 5
velocidadeYFacilPadrao = 5

velocidadeXDificilPadrao = 8
velocidadeYDificilPadrao = 8

# PARA O MODO FÁCIL
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
    
    def movimentacaoBarra2(self, alturaTotal, velocidade):
        keys = pygame.key.get_pressed()

        if keys[K_UP] and not self.yJogador <= 20:
            self.posicaoAnterior = self.yJogador
            self.yJogador -= velocidade

        if keys[K_DOWN] and not self.yJogador >= alturaTotal-(self.altura+20):
            self.posicaoAnterior = self.yJogador
            self.yJogador += velocidade
    
    def movimentacaoBarraBot(self, bola, alturaTotal, larguraTotal, velocidade):
        if bola.top < self.yJogador and not self.yJogador <= 20:
            self.posicaoAnterior = self.yJogador
            self.yJogador -= velocidade
        elif bola.bottom > self.yJogador + 80 and not self.yJogador >= alturaTotal-(self.altura+20):
            self.posicaoAnterior = self.yJogador
            self.yJogador += velocidade

##### FUNÇÕES #####
def texto(texto, posX, posY, cor, tamanhoFonte):
    num = str(texto)
    fontesys = pygame.font.SysFont(None, tamanhoFonte)
    pontuacao = fontesys.render(num, 1, cor)
    tela.blit(pontuacao,(posX, posY))

def desenhaEscolhe():
    tela.fill(preto)
    desenha_campo(cinza)
    jogador1.desenhaJogador(tela, cinza)
    jogador2.desenhaJogador(tela, cinza)
    pygame.draw.rect(tela, branco, [largura/4, altura/3, largura/2, altura/3], border_radius = 20)
    texto(0, largura/2-60, 30, cinza, 100)
    texto(0, largura/2+25, 30, cinza, 100)

def desenhaEscolheNumJogadores():
    loop = True
    numJogadores = 0
    while loop:
        desenhaEscolhe()

        texto('(1) - Um Jogador', largura/2-115, altura/2-50, preto, 45)
        texto('(2) - Dois Jogadores ', largura/2-145, altura/2+10, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loopdo = False
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    numJogadores = 1
                    loop = False
                elif evento.key == pygame.K_2:
                    numJogadores = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    loop = False
                    pygame.quit()
                    exit()

        pygame.display.update()
    return numJogadores

def desenhaEscolheDificuldade():
    loop = True
    dificuldade = 0
    while loop:
        desenhaEscolhe()
        
        texto('(F) - Fácil', largura/2-75, altura/2-50, preto, 45)
        texto('(D) - Difícil', largura/2-85, altura/2+10, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loopdo = False
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_f:
                    dificuldade = 1
                    loop = False
                elif evento.key == pygame.K_d:
                    dificuldade = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    loop = False
                    pygame.quit()
                    exit()

        pygame.display.update()
    return dificuldade

def defineVelocidade(dificuldade):
    if dificuldade == 1:
        velocidade = [velocidadeXFacilPadrao,velocidadeYFacilPadrao]
    elif dificuldade == 2:
        velocidade = [velocidadeXDificilPadrao,velocidadeYDificilPadrao]
    return velocidade

def desenha_campo(cor):
    pygame.draw.rect(tela, cor, [0, altura-20, largura, 20])
    pygame.draw.rect(tela, cor, [0, 0, largura, 20])
    pygame.draw.line(tela, cor, (largura/2,0), (largura/2,altura), 20)

def desenha_jogadores():
    jogador1.desenhaJogador(tela, branco)
    jogador2.desenhaJogador(tela, branco)

def informacoes(numeroJogadores):
    texto('ESC - Sair do Jogo',10,2,preto,26)
    texto('P - Pausa',largura-85,2,preto,26)
    if(numeroJogadores == 1):
        texto('W - Move Para Cima        S - Move Para Baixo', 10, altura-15, preto, 20)
    else:
        texto('W - Move Para Cima        S - Move Para Baixo', 10, altura-15, preto, 20)
        texto('↑ - Move Para Cima        ↓ - Move Para Baixo', largura-285, altura-15, preto, 20)

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

def placar():
    if pontuacaoJogador1 >= 10:
        texto(pontuacaoJogador1, largura/2-100, 30, branco, 100)
    else:
        texto(pontuacaoJogador1, largura/2-60, 30, branco, 100)
    texto(pontuacaoJogador2, largura/2+25, 30, branco, 100)

def jogo():
    global pontuacaoJogador1, pontuacaoJogador2, bolarect, velocidade
    
    tela.fill(preto)

    desenha_campo(branco)
    informacoes(numeroJogadores)
    desenha_jogadores()
    movimenta_jogadores()
    colisao()
    placar()
    
    bolarect = bolarect.move(velocidade)

    # VERIFICA SE A BOLA SAIU, ADICIONA O PONTO E CENTRALIZA A BOLA
    if bolarect.left < -scale:
        pontuacaoJogador2 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade = defineVelocidade(dificuldade)
        velocidade[0] = velocidade[0]
        velocidade[1] = velocidade[1]

    if bolarect.right > largura + scale:
        pontuacaoJogador1 += 1
        bolarect.center = (largura/2,altura/2)
        velocidade = defineVelocidade(dificuldade)
        velocidade[0] = -velocidade[0]
        velocidade[1] = velocidade[1]

    if bolarect.top < 20 or bolarect.bottom > altura-20:
        velocidade[1] = -velocidade[1]
    tela.blit(bola,bolarect)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loopdojogo = False
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_ESCAPE:
                loop = False
                pygame.quit()
                exit()

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
        texto("Uma produção de:", 250, 250, branco, i)
        texto("Equipe 4", 0 + (i * 6.6), 300, branco, 50)
        pygame.display.update()
        relogio.tick(100)

    pygame.time.delay(2000)

    tela.fill(preto)

    texto("P o", 310, 250, branco, tam)
    texto("ng", 430, 250, branco, tam)
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
        texto("P", 310, 250, branco, tam)
        texto("ng", 430, 250, branco, tam)
        pygame.draw.circle(tela, branco, (pos[0], pos[1]), 20, 10)

        tempo = int(pygame.time.get_ticks() / 1000)

        if tempo > 4:
            if tempo % 2 == 0:
                texto("[Aperte qualquer tecla para continuar]", largura / 3.7, altura / 1.4, branco, 30)
        pygame.display.update()
        clock.tick(60)

jogador1 = jogador(0, alturaInicialBarra, larguraJogadores, alturaJogadores)
jogador2 = jogador(largura-(larguraJogadores), alturaInicialBarra, larguraJogadores, alturaJogadores)

introducao()
numeroJogadores = desenhaEscolheNumJogadores()
dificuldade = desenhaEscolheDificuldade()
velocidade = defineVelocidade(dificuldade)

while loopdojogo:
    jogo()
