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

    def imprime(self):
        print(f'Nome - {self.nome.title()}\n'
              f'Ano: {self.ano}\n'
              f'Likes: {self.like}')


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome - {self.nome.title()}\n'
              f'Ano: {self.ano}\n'
              f'Duração: {self.duracao}\n'
              f'Likes: {self.like}')


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def imprime(self):
        print(f'Nome - {self.nome.title()}\n'
              f'Ano: {self.ano}\n'
              f'Temporada: {self.temporada}\n'
              f'Likes: {self.like}')
