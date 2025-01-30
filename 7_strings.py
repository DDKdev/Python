# concatenação de strings
a = 'Olá'
b = 'Mundo'

c = a + ' ' + b
d = 4*a
print(c, d)

# ocorrência em uma string
print('n' in b)  # true

# tamanho string
print(len(b))

# slice[inicio : final]
palavra = 'Palmeiras'
novaPalavra = palavra[0:3]
print(novaPalavra)  # Pal

# funções string BUILT IN nativas. Acionamos por ponto ' variável. '
print(palavra.upper())  # PALMEIRAS
