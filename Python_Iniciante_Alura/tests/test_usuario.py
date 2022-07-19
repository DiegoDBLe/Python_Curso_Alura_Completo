from testes_automatizados_python.leilao.dominio import Usuario, Leilao


# um usuario so pode dar um lance ate o valor da carteira, ou seja, se for um valor menor ou igual ao valor da carteira. Nunca pode dar um lance maior do
# que tem na carteira.


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    diego = Usuario('Diego', 100.0)

    leilao = Leilao('Celular')

    diego.propoe_lance(leilao, 50.0)

    assert diego.carteira == 50.0

