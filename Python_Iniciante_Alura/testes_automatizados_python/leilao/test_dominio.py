from unittest import TestCase

from testes_automatizados_python.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    # test_quando_adicionados_em_ordem_crescent_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        # Teste de uso ordem crescente
        # Criou o usuario
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        # Criou os lances dos usuarios
        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        # Criou o leilão
        leilao = Leilao('Celular')

        # Adicionou na lista de lances os lances dos usuarios
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        # valores para comparação, menor e maior valor
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # Teste de igualdade, verificar se o menor valor do lance é igual ao menor valor esperado e se o maior valor do lance é igual ao maior valor esper
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    # test_quando_adicionados_em_ordem_decrescent_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        # Esse teste testa a ordem invertida de adicionar lance na lista lances.
        # Teste de uso ordem decrescente

        # Criou o usuario
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        # Criou os lances dos usuarios
        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        # Criou o leilão
        leilao = Leilao('Celular')

        # Adicionou na lista de lances os lances dos usuarios
        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        # valores para comparação, menor e maior valor
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # Teste de igualdade, verificar se o menor valor do lance é igual ao menor valor esperado e se o maior valor do lance é igual ao maior valor esper
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)