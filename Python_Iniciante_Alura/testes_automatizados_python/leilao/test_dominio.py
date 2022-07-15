from unittest import TestCase

from testes_automatizados_python.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_avalia(self):
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
