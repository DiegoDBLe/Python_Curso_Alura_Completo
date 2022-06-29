print('*********************************')
print('Bem Vinda ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42

chute = int(input('Digite o seu número: '))

print(f'Você digitou: {chute}')

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print(f'Parabéns Você ACEROU!!')
else:
    if maior:
        print('Você Errou, Tente Novamente! Seu chute foi maior que o número secreto!')
    elif menor:
        print('Você Errou, Tente Novamente! Seu chute foi menor que o número secreto!')

print('Fim do Jogo!')
