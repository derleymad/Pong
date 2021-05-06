# -*- coding: utf-8 -*-
from Atributos import velocidadeXFacilPadrao, velocidadeYFacilPadrao, velocidadeXDificilPadrao, velocidadeYDificilPadrao
from Funcoes import velocidade_barra_bot
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