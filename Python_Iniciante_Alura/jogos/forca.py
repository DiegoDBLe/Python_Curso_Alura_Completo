import random


def jogar():

    mensagem_inicio()

    palavra_secreta = carrega_palavra_secreta()

    palavras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(palavras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 0

    imprime_quantidade_letras_palavras(palavra_secreta)

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            chute_correto(chute, palavras_acertadas, palavra_secreta)
        else:
            tentativa += 1
            if tentativa == len(palavra_secreta):
                enforcou = True
                imprime_msg_perdeu()

        if '_' not in palavras_acertadas:
            acertou = True
            if acertou:
                imprime_msg_vencedor()


def mensagem_inicio():
    print('*********************************')
    print('** Bem Vinda ao jogo de Forca! **')
    print('*********************************')


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    posicao = random.randrange(0, len(palavras))

    palavra_secreta = palavras[posicao].lower().strip()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    # for i in palavra_secreta:
    #     palavras_acertadas.append('_')
    # print(palavras_acertadas) ou
    return ['_' for i in palavra_secreta]  # Usando o List Comprehension:


def pede_chute():
    chute = input('Informe uma letra: ').lower().strip()
    return chute


def chute_correto(chute, palavras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavras_acertadas[index] = letra
        index += 1
    print(palavras_acertadas)


def imprime_msg_vencedor():
    print(f'PARABÉNS!! VOCÊ ACERTOU A PALAVRA.')


def imprime_msg_perdeu():
    print(f'INFELIZMENTE!! VOCÊ NÃO ACERTOU A PALAVRA.')


def imprime_quantidade_letras_palavras(palavra_secreta):
    print(f'Palavra com {len(palavra_secreta)} letras.')


if __name__ == '__main__':
    jogar()
