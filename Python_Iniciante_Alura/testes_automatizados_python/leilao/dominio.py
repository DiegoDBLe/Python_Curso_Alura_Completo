from testes_automatizados_python.leilao.excecoes import LanceInvalido


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
        if not self._lance_eh_valido(valor):
            raise LanceInvalido('Não pode propor lance.')

        lance = Lance(self, valor)
        leilao.propoe_lance(lance)
        self.__carteira -= valor

    def _lance_eh_valido(self, valor):
        return valor <= self.__carteira


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
            raise LanceInvalido('O mesmo usuário não pode propor dois lances seguidos')

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuario_diferente(self, lance):
        if self.__lances[-1] != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos')

    def _valor_lance_maior_que_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o anterior')

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or self._usuario_diferente(lance) and self._valor_lance_maior_que_anterior(lance)
