
def jogar():
    print('*********************************')
    print('** Bem Vinda ao jogo de Forca! **')
    print('*********************************')

    palavra_secreta = 'uva'
    palavras_acertadas = []

    # for i in palavra_secreta:
    #     palavras_acertadas.append('_')
    # print(palavras_acertadas)

    # Usando o List Comprehension:
    palavras_acertadas = ['_' for i in palavra_secreta]
    print(palavras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 0

    print(f'Palavra com {len(palavra_secreta)} letras.')
    while not enforcou and not acertou:

        chute = input('Informe uma letra: ').lower().strip()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    palavras_acertadas[index] = letra
                index += 1
            print(palavras_acertadas)
        else:
            tentativa += 1
            if tentativa == len(palavra_secreta):
                enforcou = True
                print(f'INFELIZMENTE!! VOCÊ NÃO ACERTOU A PALAVRA.')

        if '_' not in palavras_acertadas:
            acertou = True
            if acertou:
                print(f'PARABÉNS!! VOCÊ ACERTOU A PALAVRA.')

    print('Fim do Jogo!')


if __name__ == '__main__':
    jogar()
