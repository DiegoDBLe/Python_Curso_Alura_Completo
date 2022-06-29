print('*********************************')
print('Bem Vinda ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42
tentativa = 3

for rodada in range(1, tentativa + 1):
    print(f'{rodada}° Tentativa de 3')
    chute = int(input('Digite o seu número: '))

    print(f'Você digitou: {chute}')

    if chute < 1 or chute > 100:
        print('Digite um número ente 1 e 100')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f'Parabéns Você ACEROU!! Na {rodada}° tentativa.')
        break
    else:
        if maior:
            print('Você Errou, Tente Novamente! Seu chute foi maior que o número secreto!')
        elif menor:
            print('Você Errou, Tente Novamente! Seu chute foi menor que o número secreto!')
print('Fim do Jogo!')
