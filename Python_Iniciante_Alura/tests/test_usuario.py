from testes_automatizados_python.leilao.dominio import Usuario, Leilao
import pytest

# um usuario so pode dar um lance ate o valor da carteira, ou seja, se for um valor menor ou igual ao valor da carteira. Nunca pode dar um lance maior do
# que tem na carteira.


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    diego = Usuario('Diego', 100.0)

    leilao = Leilao('Celular')

    diego.propoe_lance(leilao, 50.0)

    assert diego.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira():
    diego = Usuario('Diego', 100.0)

    leilao = Leilao('Celular')

    diego.propoe_lance(leilao, 1.0)

    assert diego.carteira == 99


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira():
    diego = Usuario('Diego', 100.0)

    leilao  = Leilao('Celular')

    diego.propoe_lance(leilao, 100.0)

    assert diego.carteira == 0.0


def test_nao_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira():

    with pytest.raises(ValueError):
        diego = Usuario('Diego', 100.0)

        leilao = Leilao('Celular')

        diego.propoe_lance(leilao, 200.0)