print('*********************************')
print('Bem Vinda ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42
cont = 1
tentativa = 3

while cont <= tentativa:
    print(f'{cont}° Tentativa de 3')
    chute = int(input('Digite o seu número: '))

    print(f'Você digitou: {chute}')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f'Parabéns Você ACEROU!! Na {cont}° tentativa.')
        break
    else:
        if maior:
            print('Você Errou, Tente Novamente! Seu chute foi maior que o número secreto!')
        elif menor:
            print('Você Errou, Tente Novamente! Seu chute foi menor que o número secreto!')
    cont += 1
print('Fim do Jogo!')
