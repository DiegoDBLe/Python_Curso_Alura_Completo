from testes_automatizados_python.leilao.dominio import Leilao, Lance, Usuario, Avaliador

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

# Percorrer os lances dos usuarios
for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de R$ {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')