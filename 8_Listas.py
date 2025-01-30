elementos = ['água', 'terra', 'fogo', 'ar']
type(elementos)
len(elementos)
print(elementos[1])

animais = ['peru', 'macaco', 'ponei', 'guaxinim']

juncaoLista = elementos + animais

print(juncaoLista)

print('peru' in juncaoLista)  # true

# lista com diversos tipos de dados
Misturado = [1, 'água', 13]


# listas BUILT IN
elementos = ['água', 'terra', 'fogo', 'ar']
elementos.append('visão')  # adiciona um novo item no FINAL
elementos.index('visão')  # Puxa o índice
elementos.count('água')  # quantas ocorrências
elementos.insert(2, 'banana')  # insere na posição indicada (2)
elementos.sort()  # ordenação
elementos.reverse()  # ordenação reversa
