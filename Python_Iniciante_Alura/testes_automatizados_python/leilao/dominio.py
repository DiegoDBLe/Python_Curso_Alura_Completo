
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
        if self._lance_eh_valido(valor):
            raise ValueError('Saldo insuficiente!! Não pode propor lance.')

        lance = Lance(self, valor)
        leilao.propoe_lance(lance)
        self.__carteira -= valor

    def _lance_eh_valido(self, valor):
        return valor > self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe_lance(self, lance: Lance):

        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('O mesmo usuário não pode propor dois lances seguidos')

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuario_diferente(self, lance):
        return self.__lances[-1] != lance.usuario

    def _valor_lance_maior_que_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or self._usuario_diferente(lance) and self._valor_lance_maior_que_anterior(lance)
