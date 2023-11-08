from codigo.jogo import brincadeira
from pytest import mark


def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1
    esperado = 1
    resultado = brincadeira(entrada)
    assert resultado == esperado

    assert(brincadeira(1) == 1)


@mark.testenew
def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2