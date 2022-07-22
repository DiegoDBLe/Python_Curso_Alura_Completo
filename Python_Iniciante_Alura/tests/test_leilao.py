from unittest import TestCase

from testes_automatizados_python.leilao.dominio import Usuario, Lance, Leilao
from testes_automatizados_python.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        # Teste de uso ordem crescente
        # Criou o usuario
        self.gui = Usuario('Gui', 500.0)

        # Criou os lances dos usuarios
        self.lance_do_gui = Lance(self.gui, 150.0)

        # Criou o leilão
        self.leilao = Leilao('Celular')

    # test_quando_adicionados_em_ordem_crescent_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('yuri', 500.0)

        lance_do_yuri = Lance(yuri, 200.0)

        # Adicionou na lista de lances os lances dos usuarios
        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_do_yuri)

        # # valores para comparação, menor e maior valor
        # menor_valor_esperado = 100.0
        # maior_valor_esperado = 150.0
        #
        # # Teste de igualdade, verificar se o menor valor do lance é igual ao menor valor esperado e se o maior valor do lance é igual ao maior valor esper
        # self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        # self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # test_quando_adicionados_em_ordem_decrescent_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe_lance(self.lance_do_gui)
            self.leilao.propoe_lance(lance_do_yuri)

    # test_quando_leilao_tiver_um_lance_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        # Adicionar o lance na lista de lancers
        self.leilao.propoe_lance(self.lance_do_gui)

        # Verificar se o valor que estamos esperando é igual ao menor lance e maior lance
        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    # test_quando_o_leilao_tiver_tres_lances_deve_retornar_o_maior_e_o_menor_valor
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        levi = Usuario('Levi', 500.0)
        yuri = Usuario('yuri', 500.0)

        lance_do_levi = Lance(levi, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe_lance(lance_do_yuri)
        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_do_levi)

        # menor_valor_esperado = 100.0
        # maior_valor_esperado = 200.0
        #
        # self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        # self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # teste_quando_leilao_nao_tiver_lances_deve_permitir_propor_um_lance
    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe_lance(self.lance_do_gui)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances)

    # test_quando_o_ultimo_usuario_for_diferente_deve_permitir_propor_um_lance
    def test_caso_ultimo_usuario_for_diferente_deve_permitir_propor_um_lance(self):
        yuri = Usuario('Yuri',500.0)

        lance_yuri = Lance(yuri, 200.0)

        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_yuri)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    # test_quando_o_ultimo_usuario_for_o_mesmo_nao_deve_permitir_propor_um_lance
    def test_nao_deve_permitir_propor_um_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_gui_segundo = Lance(self.lance_do_gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe_lance(self.lance_do_gui)
            self.leilao.propoe_lance(lance_gui_segundo)
