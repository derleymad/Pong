from Player import *

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

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
    jogador1.desenhaJogador(tela, branco)
    jogador2.desenhaJogador(tela, branco)

def desenhaEscolhe():
    tela.fill(preto)
    desenha_campo(cinza)
    jogador1.desenhaJogador(tela, cinza)
    jogador2.desenhaJogador(tela, cinza)
    pygame.draw.rect(tela, branco, [largura / 4, altura / 3, largura / 2, altura / 3], border_radius=20)
    texto(0, largura / 2 - 60, 30, cinza, 100)
    texto(0, largura / 2 + 25, 30, cinza, 100)

def escolheNumJogadores():
    loop = True
    numJogadores = 0
    while loop:
        desenhaEscolhe()

        texto('(1) - Um Jogador', largura / 2 - 115, altura / 2 - 50, preto, 45)
        texto('(2) - Dois Jogadores ', largura / 2 - 145, altura / 2 + 10, preto, 45)

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

def defineVelocidade(dificuldade):
    if dificuldade == 1:
        velocidade = [velocidadeXFacilPadrao, velocidadeYFacilPadrao]
    elif dificuldade == 2:
        velocidade = [velocidadeXDificilPadrao, velocidadeYDificilPadrao]
    return velocidade

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

def pausa():
    loop = True
    escolha = 0
    while loop:
        pygame.draw.rect(tela, branco, [largura / 4, altura / 3, largura / 2, altura / 3], border_radius=20)

        texto('(R) - Reiniciar Partida', largura / 2 - 155, altura / 2 - 50, preto, 45)
        texto('(ESC) - Sair', largura / 2 - 90, altura / 2 + 10, preto, 45)

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
