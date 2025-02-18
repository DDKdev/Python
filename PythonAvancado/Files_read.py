# testar no arquivo na área de trabalho pois devido ao tamnho no caminho o debugger não consegue chegar ao arquivo de texto.


#OPEN e READ
letra = open('texto.txt', 'r')
print(letra.read(10)) # retorna 10 caracteres
print(letra.read()) # todo o arquivo
print(letra.readline())#primeira linha
print(letra.readlines()) # todas as linhas em uma LISTA
print(len(letra.readlines())) # quantidade de linhas

# contando PALAVRAS
palavras = letra.read()
lista_palavras = palavras.split() # lista com todas as palavras separadas por indice
print(lista_palavras) 
print(len(lista_palavras)) # quantidade de palavras
palavras_sem_repetir = set(lista_palavras)
print(len(palavras_sem_repetir)) # quantidade de palavras distintas

print(lista_palavras.count('sina')) # contagem de ocorrências










