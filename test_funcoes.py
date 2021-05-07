# -*- coding: utf-8 -*-
from Atributos import velocidadeXFacilPadrao, velocidadeYFacilPadrao, velocidadeXDificilPadrao, velocidadeYDificilPadrao
from Funcoes import velocidade_barra_bot, velocidade_barra_jogadores, jogador1, jogador2
from Bola import define_velocidade_da_bola
import pytest

# Caixa Preta
def test_velocidade_facil():
    assert define_velocidade_da_bola(1) == [velocidadeXFacilPadrao, velocidadeYFacilPadrao]

def test_velocidade_dificil():
    assert define_velocidade_da_bola(2) == [velocidadeXDificilPadrao, velocidadeYDificilPadrao]

def test_velocidade_barra_bot_1():
    assert velocidade_barra_bot(1) == 4.5

def test_velocidade_barra_bot_2():
    assert velocidade_barra_bot(2) == 7.43

def test_velocidade_barra_bot_3():
    assert velocidade_barra_bot(3) == 0

def test_velocidade_barra_bot_4():
    assert velocidade_barra_bot(-1) == 0

def test_velocidade_barra_quando_temos_um_jogador_e_dificuldade_facil():
    velocidade_barra_jogadores(1, 1)
    assert jogador1.velocidade == 5

def test_velocidade_barra_quando_temos_um_jogador_e_dificuldade_dificil():
    velocidade_barra_jogadores(1, 2)
    assert jogador1.velocidade == 5.5

def test_velocidade_barra_quando_temos_dois_jogadores_e_dificuldade_facil():
    velocidade_barra_jogadores(2, 1)
    assert jogador1.velocidade == 5
    assert jogador2.velocidade == 5

def test_velocidade_barra_quando_temos_dois_jogadores_e_dificuldade_dificil():
    velocidade_barra_jogadores(2, 2)
    assert jogador1.velocidade == 5.5
    assert jogador2.velocidade == 5.5

# Caixa Branca
def test_velocidade_barra_bot_facil():
    assert velocidade_barra_bot(1) == 4.5

def test_velocidade_barra_bot_dificil():
    assert velocidade_barra_bot(2) == 7.43

def test_velocidade_barra_bot_invalido():
    assert velocidade_barra_bot(3) == 0

def test_velocidade_facil():
    assert define_velocidade_da_bola(1) == [velocidadeXFacilPadrao, velocidadeYFacilPadrao]

def test_velocidade_dificil():
    assert define_velocidade_da_bola(2) == [velocidadeXDificilPadrao, velocidadeYDificilPadrao]

def test_velocidade_invalido():
    assert define_velocidade_da_bola(-5) == 0
