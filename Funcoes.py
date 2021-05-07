# -*- coding: utf-8 -*-
from Atributos import *
from Player import *
from Bola import *

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

jogador1 = Jogador(0, alturaInicialBarra, larguraJogadores, alturaJogadores, 0, 5)
jogador2 = Jogador(largura - (larguraJogadores), alturaInicialBarra, larguraJogadores, alturaJogadores, 0, 5)

def texto(texto, posX, posY, cor, tamanhoFonte):
    num = str(texto)
    fontesys = pygame.font.SysFont(None, tamanhoFonte)
    pontuacao = fontesys.render(num, 1, cor)
    tela.blit(pontuacao, (posX, posY))

def desenha_campo(cor):
    pygame.draw.rect(tela, cor, [0, altura - 20, largura, 20])
    pygame.draw.rect(tela, cor, [0, 0, largura, 20])
    pygame.draw.line(tela, cor, (largura / 2, 0), (largura / 2, altura), 20)

def desenha_jogadores():
    jogador1.desenha_jogador(tela, branco)
    jogador2.desenha_jogador(tela, branco)

def desenha_escolhe():
    tela.fill(preto)
    desenha_campo(cinza)
    jogador1.desenha_jogador(tela, cinza)
    jogador2.desenha_jogador(tela, cinza)
    pygame.draw.rect(tela, branco, [largura / 4, altura / 3, largura / 2, altura / 3], border_radius=20)
    texto(0, largura / 2 - 60, 30, cinza, 100)
    texto(0, largura / 2 + 25, 30, cinza, 100)

def escolhe_numero_jogadores():
    loop = True
    numJogadores = 0
    while loop:
        desenha_escolhe()

        texto('(1) - Um Jogador', largura / 2 - 115, altura / 2 - 50, preto, 45)
        texto('(2) - Dois Jogadores ', largura / 2 - 145, altura / 2 + 10, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                numJogadores = 0
                loop = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    numJogadores = 1
                    loop = False
                elif evento.key == pygame.K_2:
                    numJogadores = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    numJogadores = 0
                    loop = False

        pygame.display.update()
    return numJogadores

def placar():
    if jogador1.pontuacao >= 10:
        texto(jogador1.pontuacao, largura / 2 - 100, 30, branco, 100)
    else:
        texto(jogador1.pontuacao, largura / 2 - 60, 30, branco, 100)
    texto(jogador2.pontuacao, largura / 2 + 25, 30, branco, 100)

def informacoes(numeroJogadores):
    texto('ESC - Sair do Jogo', 10, 2, preto, 26)
    texto('P - Pausa', largura - 85, 2, preto, 26)
    if (numeroJogadores == 1):
        texto('W - Move Para Cima        S - Move Para Baixo', 10, altura - 15, preto, 20)
    else:
        texto('W - Move Para Cima        S - Move Para Baixo', 10, altura - 15, preto, 20)
        texto('I - Move Para Cima        J - Move Para Baixo', largura - 285, altura - 15, preto, 20)

def introducao():
    global preto, branco, altura, G, relogio

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sair_do_jogo(0)

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
                sair_do_jogo(0)
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

def pausa():
    loop = True
    escolha = 0
    while loop:
        pygame.draw.rect(tela, branco, [largura / 4, altura / 3, largura / 2, altura / 3], border_radius=20)

        texto('(R) - Reiniciar Partida', largura / 2 - 155, altura / 2 - 50, preto, 45)
        texto('(ESC) - Sair', largura / 2 - 90, altura / 2 + 10, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                escolha = 0
                loop = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    escolha = 1
                    loop = False
                elif evento.key == pygame.K_r:
                    escolha = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    escolha = 0
                    loop = False

        pygame.display.update()
    return escolha

def fim_de_jogo():
    loop = True
    escolha = 0
    while loop:
        tela.fill(preto)
        pygame.draw.rect(tela, branco, [largura / 4, altura / 3 + 30, largura / 2, altura / 3], border_radius=20)

        texto('FIM DE JOGO', largura / 2 - 220, altura / 2 - 200, branco, 100)

        if jogador1.pontuacao == 10:
            texto('JOGADOR 1 VENCEU', largura / 2 - 180, altura / 2 - 120, branco, 50)
        elif jogador2.pontuacao == 10:
            texto('JOGADOR 2 VENCEU', largura / 2 - 180, altura / 2 - 120, branco, 50)

        texto('(R) - Jogar Novamente', largura / 2 - 155, altura / 2 - 20, preto, 45)
        texto('(ESC) - Sair', largura / 2 - 90, altura / 2 + 40, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                escolha = 0
                loop = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    escolha = 1
                    loop = False
                if evento.key == K_ESCAPE:
                    escolha = 0
                    loop = False

        pygame.display.update()
    return escolha

def escolhe_dificuldade():
    loop = True
    dificuldade = 0
    while loop:
        desenha_escolhe()

        texto('(F) - Fácil', largura / 2 - 75, altura / 2 - 50, preto, 45)
        texto('(D) - Difícil', largura / 2 - 85, altura / 2 + 10, preto, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                dificuldade = 0
                loop = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_f:
                    dificuldade = 1
                    loop = False
                elif evento.key == pygame.K_d:
                    dificuldade = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    dificuldade = 0
                    loop = False

        pygame.display.update()
    return dificuldade

def movimenta_jogadores(bolarect, numeroJogadores):
    if numeroJogadores == 1:
        jogador1.movimentacao_barra_1(altura)
        jogador2.movimentacao_barra_bot(bolarect, altura, largura)
    else:
        jogador1.movimentacao_barra_1(altura)
        jogador2.movimentacao_barra_2(altura)

def velocidade_barra_bot(dificuldade):
    if dificuldade == 1:
        velocidade = 4.5
    elif dificuldade == 2:
        velocidade = 7.43
    else: 
        velocidade = 0
    return velocidade

def velocidade_barra_jogadores(numeroJogadores, dificuldade):
    if dificuldade == 1:
        jogador1.velocidade = 5
        if numeroJogadores == 1:
            jogador2.velocidade = velocidade_barra_bot(dificuldade)
        else:
            jogador2.velocidade = 5
    elif dificuldade == 2:
        jogador1.velocidade = 5.5
        if numeroJogadores == 1:
            jogador2.velocidade = velocidade_barra_bot(dificuldade)
        else:
            jogador2.velocidade = 5.5

def colisao(bolarect, velocidade):
    if bolarect.bottom > jogador1.yJogador and bolarect.top < jogador1.yJogador + jogador1.altura:
        if velocidade[0] < 0 and bolarect.left < jogador1.xJogador + jogador1.largura:
            velocidade[0] = -velocidade[0]

    if bolarect.bottom > jogador2.yJogador and bolarect.top < jogador2.yJogador + jogador2.altura:
        if velocidade[0] > 0 and bolarect.right > jogador2.xJogador:
            velocidade[0] = -velocidade[0]

def sair_do_jogo(numero):
    if(numero == 0):
        pygame.quit()
        exit()