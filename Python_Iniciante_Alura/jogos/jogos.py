import adivinhacao
import forca

print('*********************************')
print('******* Escolha um Jogo! ********')
print('*********************************')

print('(1) Jogo da Adivinhação\n'
      '(2) Jogo da Forca')

jogo = int(input('Qual jogo deseja jogar? '))

if jogo == 1:
    print('Iniciando jogo da Adivinhação...')
    adivinhacao.jogar()
elif jogo == 2:
    print('Iniciando jogo da Forca...')
    forca.jogar()
