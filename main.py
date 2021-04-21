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

reinicia = 0

branco = (255,255,255)
preto = (0,0,0,0)
cinza = (25,25,25)

velocidadeXFacilPadrao = 5
velocidadeYFacilPadrao = 5

velocidadeXDificilPadrao = 8
velocidadeYDificilPadrao = 8

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

        if keys[K_s] and not self.yJogador >= alturaTotal-(self.altura+20):
            self.yJogador += velocidade
    
    def movimentacaoBarra2(self, alturaTotal, velocidade):
        keys = pygame.key.get_pressed()
        if keys[K_i] and not self.yJogador <= 20:
            self.yJogador -= velocidade

        if keys[K_j] and not self.yJogador >= alturaTotal-(self.altura+20):
            self.yJogador += velocidade
    
    def movimentacaoBarraBot(self, bola, alturaTotal, larguraTotal, velocidade):
        if bola.top < self.yJogador and not self.yJogador <= 20:
            self.yJogador -= velocidade
        elif bola.bottom > self.yJogador + 80 and not self.yJogador >= alturaTotal-(self.altura+20):
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

def escolheNumJogadores():
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

def escolheDificuldade():
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
                    jogador1.velocidade = 5
                    jogador2.velocidade = 5
                    dificuldade = 1
                    loop = False
                elif evento.key == pygame.K_d:
                    jogador1.velocidade = 6
                    jogador2.velocidade = 6
                    dificuldade = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    loop = False
                    pygame.quit()
                    exit()

        pygame.display.update()
    return dificuldade

def pausa():
    loop = True
    escolha = 0
    while loop:
        pygame.draw.rect(tela, branco, [largura/4, altura/3, largura/2, altura/3], border_radius = 20)
        
        texto('(R) - Reiniciar Partida', largura/2-155, altura/2-50, preto, 45)
        texto('(ESC) - Sair', largura/2-90, altura/2+10, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loopdo = False
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    escolha = 1
                    loop = False
                elif evento.key == pygame.K_r:
                    escolha = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    loop = False
                    pygame.quit()
                    exit()

        pygame.display.update()
    return escolha

def fimDeJogo():
    loop = True
    escolha = 0
    while loop:
        tela.fill(preto)
        pygame.draw.rect(tela, branco, [largura/4, altura/3+30, largura/2, altura/3], border_radius = 20)

        texto('FIM DE JOGO', largura/2-220, altura/2-200, branco, 100)

        if jogador1.pontuacao == 10:
            texto('JOGADOR 1 VENCEU', largura/2-180, altura/2-120, branco, 50)
        elif jogador2.pontuacao == 10:
            texto('JOGADOR 2 VENCEU', largura/2-180, altura/2-120, branco, 50)
        
        texto('(R) - Jogar Novamente', largura/2-155, altura/2-20, preto, 45)
        texto('(ESC) - Sair', largura/2-90, altura/2+40, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loopdo = False
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    escolha = 1
                    loop = False
                elif evento.key == pygame.K_r:
                    escolha = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    loop = False
                    pygame.quit()
                    exit()

        pygame.display.update()
    return escolha

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
        texto('I - Move Para Cima        J - Move Para Baixo', largura-285, altura-15, preto, 20)

def movimenta_jogadores():
    if numeroJogadores == 1:
        jogador1.movimentacaoBarra1(altura, jogador1.velocidade)
        jogador2.movimentacaoBarraBot(bolarect ,altura, largura, jogador2.velocidade)
    else:
        jogador1.movimentacaoBarra1(altura, jogador1.velocidade)
        jogador2.movimentacaoBarra2(altura, jogador2.velocidade)

def colisao():
    if bolarect.bottom > jogador1.yJogador and bolarect.top < jogador1.yJogador + jogador1.altura:
        if velocidade[0] < 0 and bolarect.left < jogador1.xJogador+jogador1.largura:
            velocidade[0] = -velocidade[0]
    
    if bolarect.bottom > jogador2.yJogador and bolarect.top < jogador2.yJogador + jogador2.altura:
        if velocidade[0] > 0 and bolarect.right > jogador2.xJogador:
            velocidade[0] = -velocidade[0]

def placar():
    if jogador1.pontuacao >= 10:
        texto(jogador1.pontuacao, largura/2-100, 30, branco, 100)
    else:
        texto(jogador1.pontuacao, largura/2-60, 30, branco, 100)
    texto(jogador2.pontuacao, largura/2+25, 30, branco, 100)
    
def jogo():
    global bolarect, velocidade
    
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
        jogador2.pontuacao += 1
        bolarect.center = (largura/2,altura/2)
        velocidade = defineVelocidade(dificuldade)
        velocidade[0] = velocidade[0]
        velocidade[1] = velocidade[1]

    if bolarect.right > largura + scale:
        jogador1.pontuacao += 1
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
    global preto, branco, altura, velocidade, G, relogio

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

jogador1 = jogador(0, alturaInicialBarra, larguraJogadores, alturaJogadores,0, 5)
jogador2 = jogador(largura-(larguraJogadores), alturaInicialBarra, larguraJogadores, alturaJogadores, 0, 5)

introducao()
numeroJogadores = escolheNumJogadores()
dificuldade = escolheDificuldade()
velocidade = defineVelocidade(dificuldade)

while loopdojogo:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_p:
                pause = True
                while pause:
                    escolha = pausa()
                    if escolha == 1:
                        pause = False
                    elif escolha == 2:
                        reinicia += 1
                        pause = False
    
    if jogador1.pontuacao == 10 or jogador2.pontuacao == 10:
        fimJogo = True
        while fimJogo:
            escolha = fimDeJogo()
            if escolha == 1:
                fimJogo = False
            elif escolha == 2:
                reinicia += 1
                fimJogo = False

    if reinicia == 1:
        reinicia = 0
        jogador1.pontuacao = 0
        jogador2.pontuacao = 0
        jogador1.yJogador = alturaInicialBarra
        jogador2.yJogador = alturaInicialBarra
        bolarect.center = (largura/2,altura/2)
        numeroJogadores = escolheNumJogadores()
        dificuldade = escolheDificuldade()
        velocidade = defineVelocidade(dificuldade)

    jogo()
