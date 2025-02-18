# dicionario é uma lista não ordenada
# armazena chave:valor
# pode armazenar lista de valores

# criando dicionários {chave: valor}

dicionario1 = {'01':'Daniel'}

# dicionario que armazena lista
dic_lista = {'02':['Saulo',"magalhães"],
             '03':['Adriana', 'calcanhoto'],
             '04':['Roverval', 'de andrade']}

#print dos dicionarios
#para acessar um único item da lista pode-se usar o [indice] após a indicação da chave '03'
print(dicionario1['01'], dic_lista['03'][0])

#adicionando um novo item na dic_lista (2 maneiras)
dic_lista['05'] = ['Aline','Albuquerque']
# .setdefault - permite incluir um item na lista já verificando previamente se já existe a chave.
dic_lista.setdefault('06',['Fulano de tal'])

print('05'in dic_lista)
print(dic_lista)

#apagando um item do dicionario del( )
del (dic_lista['02'])
print(dic_lista)


# usando método .get - permite acessar um valor e se não existir retornar um valor padrão
# Exemplo de uso do método get em um dicionário
dicionario = {'nome': 'Ana', 'idade': 28, 'cidade': 'São Paulo'}

# Tentando acessar uma chave que existe
nome = dicionario.get('nome')
print(nome)  # Saída: Ana

# Tentando acessar uma chave que não existe com um valor padrão
telefone = dicionario.get('telefone', 'Não disponível')
print(telefone)  # Saída: Não disponível


#UPDATE juntando dois dicionarios - NÃO PODE EXISTIR CHAVES IGUAIS nas duas listas
dic_Um = {'01':['água','mar', 'ney'],
          '02':['fogo','inferno', 'vizinho']}
dic_Dois = {'03':['Ar','Nuvem', 'oxigênio'],
          '04':['terra','caiu', 'deslizou']}
dic_Um.update(dic_Dois)
print(dic_Um)

# Para armazenar a nova lista em outra, isso altera a lista orginal
dic_tres = dic_Um.copy()
dic_Um.update(dic_Dois)
print(dic_tres)

# Copia profunda que não altera a lista original - testar no arquivo copy.py AQUI NÃO  aparece no terminal
grupo1 = {'01':'palmeiras','02':'Corinthians'}
import copy
grupo2 = copy.deepcopy(grupo1)
grupo2['03'] ='Santos'
print(grupo1)
print(grupo2)





#MÉTODO keys()
dias={'seg': 'segunda', 'ter':'terça', 'qua':'quarta'}
chaves = dias.keys()

for chave in chaves:
    print(chave)

#MÉTODO values()
values = dias.values()

for value in values:
    print(value)

#MÉTODO items()
items = dias.items()

for item in items:
    print(item)

#método POP() - exclusão de um item
dias.pop('qua')
print(dias)