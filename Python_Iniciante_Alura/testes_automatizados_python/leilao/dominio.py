import sys


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome

    def propoe_lance(self, leilao, valor):
        lance = Lance(self, valor)
        leilao.propoe_lance(lance)
        self.__carteira -= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe_lance(self, lance: Lance):
        # se a lista estiver vazia ou o ultimo usuario q deu o lance na lista for diferente e se o ultimo lance     :
        # verificar qual o lance maior ou menor
        # adiciona o lance na lista
        if not self.__lances or self.__lances[-1] != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError('O mesmo usuário não pode propor dois lances seguidos')

    @property
    def lances(self):
        return self.__lances[:]
