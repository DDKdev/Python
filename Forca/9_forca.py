import random

# Criar lista de palavras para o jogo
lista_palavras = ['Palmeiras', 'Salada', 'Argentina', 'Guatemala', 'Antena']

# Escolha da palavra
palavra_sorteada = random.choice(lista_palavras)
# print(palavra_sorteada)

# Criação dos campos da forca
palavra_escondida = ' _ ' * len(palavra_sorteada)
palavra_escondida = palavra_escondida.replace(" ", "")

# Criação da lista que armazena as letras citadas
letras_adivinhadas = []
max_tentativas = 10

while True:
    # Mostra na tela a palavra escondida
    print(palavra_escondida.replace("", " ")[1:-1])
    # Usuário digita uma letra
    letra = input('Digite uma letra: ')

    # Verificamos se a letra já consta na lista_letras
    if letra.lower() in letras_adivinhadas:
        # Pedir para digitar outra vez, sem descontar a tentativa
        print('Essa letra já foi digitada. Tente outra.')
        continue

    letras_adivinhadas.append(letra.lower())

    # Se a letra digitada está na palavra
    if letra.lower() in palavra_sorteada.lower():
        lista = list(palavra_escondida)
        for indice in range(len(palavra_sorteada)):
            if letra.lower() == palavra_sorteada[indice].lower():
                lista[indice] = palavra_sorteada[indice]
        palavra_escondida = ''.join(lista)
    else:
        max_tentativas -= 1
        print(f'Letra não encontrada. Você tem {max_tentativas} tentativas.')

    # Verificar se o usuário ganhou
    if palavra_escondida.lower() == palavra_sorteada.lower():
        print('Parabéns, você ganhou!')
        break
    elif max_tentativas == 0:
        print('Acabaram suas tentativas.')

        print(f'A palavra era: {palavra_sorteada}.')
        break
