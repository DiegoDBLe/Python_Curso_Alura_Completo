class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome - {self.nome.title()}\nAno: {self.ano}\nLikes: {self.like}'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome - {self.nome.title()}\nAno: {self.ano}\nDuração: {self.duracao}\nLikes: {self.like}'


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome - {self.nome.title()}\nAno: {self.ano}\nTemporada: {self.temporada}\nLikes: {self.like}'
