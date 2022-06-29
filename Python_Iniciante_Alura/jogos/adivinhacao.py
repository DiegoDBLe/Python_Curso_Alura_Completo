import random

print('*********************************')
print('Bem Vinda ao jogo de Adivinhação!')
print('*********************************')
print('***** Niveis *****\n'
      'Fácil Digite (1)\n'
      'Médio Digite (2)\n'
      'Difícil Digite (3)')

numero_secreto = random.randint(1, 100)
tentativa = 0
pontos = 1000
print(numero_secreto)
nivel = int(input('Escolha o Nivel: '))

if nivel == 1:
    tentativa = 15
elif nivel == 2:
    tentativa = 10
elif nivel == 3:
    tentativa = 5
else:
    print('Número Inválido!')

for rodada in range(1, tentativa + 1):
    print(f'{rodada}° Tentativa de {tentativa}')
    chute = int(input('Digite o seu número: '))

    print(f'Você digitou: {chute}')

    if chute < 1 or chute > 100:
        print('Digite um número ente 1 e 100')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f'Parabéns Você ACEROU!! Na {rodada}° tentativa e fez {pontos} pontos.')
        break
    else:
        if maior:
            print('Você Errou, Tente Novamente! Seu chute foi maior que o número secreto!')
        elif menor:
            print('Você Errou, Tente Novamente! Seu chute foi menor que o número secreto!')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
print('Fim do Jogo!')
