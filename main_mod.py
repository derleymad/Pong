from Funcoes import *
from Player import *
from Bola import *

pygame.init()

##### FUNÇÕES #####
def escolheDificuldade():
    global velocidadePadraoBot
    loop = True
    dificuldade = 0
    while loop:
        desenhaEscolhe()

        texto('(F) - Fácil', largura / 2 - 75, altura / 2 - 50, preto, 45)
        texto('(D) - Difícil', largura / 2 - 85, altura / 2 + 10, preto, 45)

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
                    jogador1.velocidade = 5.5
                    jogador2.velocidade = 5.5
                    velocidadePadraoBot = 7.43
                    dificuldade = 2
                    loop = False
                if evento.key == K_ESCAPE:
                    loop = False
                    pygame.quit()
                    exit()

        pygame.display.update()
    return dificuldade

def movimenta_jogadores():
    if numeroJogadores == 1:
        jogador1.movimentacaoBarra1(altura, jogador1.velocidade)
        jogador2.movimentacaoBarraBot(bolarect, altura, largura, velocidadePadraoBot)
    else:
        jogador1.movimentacaoBarra1(altura, jogador1.velocidade)
        jogador2.movimentacaoBarra2(altura, jogador2.velocidade)


def colisao():
    if bolarect.bottom > jogador1.yJogador and bolarect.top < jogador1.yJogador + jogador1.altura:
        if velocidade[0] < 0 and bolarect.left < jogador1.xJogador + jogador1.largura:
            velocidade[0] = -velocidade[0]

    if bolarect.bottom > jogador2.yJogador and bolarect.top < jogador2.yJogador + jogador2.altura:
        if velocidade[0] > 0 and bolarect.right > jogador2.xJogador:
            velocidade[0] = -velocidade[0]


##### ISSO PODE FICAR NO MAIN #####
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
        bolarect.center = (largura / 2, altura / 2)
        velocidade = defineVelocidade(dificuldade)
        velocidade[0] = velocidade[0]
        velocidade[1] = velocidade[1]

    if bolarect.right > largura + scale:
        jogador1.pontuacao += 1
        bolarect.center = (largura / 2, altura / 2)
        velocidade = defineVelocidade(dificuldade)
        velocidade[0] = -velocidade[0]
        velocidade[1] = velocidade[1]

    if bolarect.top < 20 or bolarect.bottom > altura - 20:
        velocidade[1] = -velocidade[1]
    tela.blit(bola, bolarect)

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

    # ESPERA CERTOS MILÉSIMOS SUFICIENTE PARA TER 60 FPS
    relogio.tick(60)

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
        bolarect.center = (largura / 2, altura / 2)
        numeroJogadores = escolheNumJogadores()
        dificuldade = escolheDificuldade()
        velocidade = defineVelocidade(dificuldade)

    jogo()
