
class Filme:

    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.like = 0

    def dar_like(self):
        self.like += 1

    def nome_filme(self):
        print(f'Nome - {self.nome.title()}\n'
              f'Ano: {self.ano}\n'
              f'Duração: {self.duracao}\n'
              f'Likes: {self.like}')


class Serie:

    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada
        self.like = 0

    def dar_like(self):
        self.like += 1

    def nome_serie(self):
        print(f'Nome - {self.nome.title()}\n'
              f'Ano - {self.ano}\n'
              f'Temporadas - {self.temporada}\n'
              f'Likes: {self.like}')