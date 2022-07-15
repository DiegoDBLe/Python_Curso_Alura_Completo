from unittest import TestCase

from testes_automatizados_python.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        # Teste de uso ordem crescente
        # Criou o usuario
        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')

        # Criou os lances dos usuarios
        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)

        # Criou o leilão
        self.leilao = Leilao('Celular')

    # test_quando_adicionados_em_ordem_crescent_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        # Adicionou na lista de lances os lances dos usuarios
        self.leilao.lances.append(self.lance_do_yuri)
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

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

        # Adicionou na lista de lances os lances dos usuarios
        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(self.lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        # valores para comparação, menor e maior valor
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # Teste de igualdade, verificar se o menor valor do lance é igual ao menor valor esperado e se o maior valor do lance é igual ao maior valor esper
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    # test_quando_leilao_tiver_um_lance_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):

        # Adicionar o lance na lista de lancers
        self.leilao.lances.append(self.lance_do_gui)

        # Avaliar o lance
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        # Verificar se o valor que estamos esperando é igual ao menor lance e maior lance
        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    # test_quando_o_leilao_tiver_tres_lances_deve_retornar_o_maior_e_o_menor_valor
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        levi = Usuario('Levi')

        lance_do_levi = Lance(levi, 200.0)

        leilao = Leilao('Celular')

        leilao.lances.append(self.lance_do_gui)
        leilao.lances.append(self.lance_do_yuri)
        leilao.lances.append(lance_do_levi)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

