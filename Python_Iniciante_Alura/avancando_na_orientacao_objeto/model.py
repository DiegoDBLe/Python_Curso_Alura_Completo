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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


vingadores = Filme('vingadores guerra infita', 2018, 160)
tmep = Filme('todo mundo em panico', 1999, 100)

atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2010, 2)

vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, tmep, atlanta, demolidor]

playlista_fds = Playlist('playlist fim-de-semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlista_fds)}')
for programa in playlista_fds:
    print(programa)

