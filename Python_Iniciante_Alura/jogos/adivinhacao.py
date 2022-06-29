print('*********************************')
print('Bem Vinda ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42

chute = int(input('Digite o seu número: '))

print(f'Você digitou: {chute}')

if chute == numero_secreto:
    print(f'Parabéns Você ACEROU!!')
else:
    print('Você Errou, Tente Novamente!')

print('Fim do Jogo!')