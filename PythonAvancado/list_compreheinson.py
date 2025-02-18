#LIST COMPREHENSION A PARTIR DE UMA LISTA
animais = ['cachorro', 'peixe','gato','papagaio', 'dinossauro']
# [ conteúdo PARA CADA item DENTRO DE lista CONDIÇÃO]
# [ listaComAnimais PARA CADA animal DENTRO DE animais SE tiverem 'r' no nome ]
nova_lista = [animal for animal in animais if 'r' in animal]
print(nova_lista)

salarios= [1000,2000,3000,4000,5000]
#Aumento de 20% para aqueles que ganham menos ou igual a 3000
novos_salarios =[salario*1.2 for salario in salarios if salario <= 3000]
print(novos_salarios)


# LIST COMPREHEISON COM RANGE
numeros_pares = [numero for numero in range(10) if numero%2 == 0]
print(numeros_pares)

# LIST COMPREHEISON COM FUNÇÕES BULT IN
nomes_Upper =[animal.upper() for animal in animais if 'e' in animal]
print(nomes_Upper)

#LIST COMPREHEINSON com ELSE
# o teste consiste em: RETORNE NOME DA FRUTA SE FRUTA TER O NOEM DIFERENTE DE BANANA. POIS SE FOR IGUAL A BANANA SUBSTITUA POR "DOCE" E VAI FAZER ISSO COM CADA FRUTA DENTRO DA LISTA FRUTAS
frutas = ['banana', 'maçã', 'laranja', 'manga']
novas_frutas = [fruta if fruta != 'banana' else 'DOCE' for fruta in frutas]
print(novas_frutas)