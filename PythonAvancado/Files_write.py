with open ('text2.txt', 'w') as file:
    file.write('Olá \n')
    file.write('palmeirense')

with open ('text2.txt', 'a') as file:
    file.write('Tudo tranquilo \n')


# 'w' sobrescreve todo o arquivo txt, pois o cursor é posicionado no início.
# 'a' adiciona no fim do documento.

