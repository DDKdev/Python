for dia in ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']:
    print(dia)

numeroParatabuada = int(input('Digite o número da tabuada: '))
qtdelinhas = 11
for multiplicadorLinha in range(0, qtdelinhas):
    print(f'A resultado de {numeroParatabuada} x {
          multiplicadorLinha} é: {numeroParatabuada*multiplicadorLinha}')

# FIBONACCI
n = int(input("digite a posição na lista de fibonacci que deve aparecer: "))
primeiro = 1
segundo = 1

if n == 1 or n == 2:
    print('1')
else:
    for _ in range(2, n):
        elemento = primeiro + segundo
        primeiro = segundo
        segundo = elemento
    print(elemento)

# TESTE DE MESA
# n = 5

# range = 2
# elemento = 1 + 1
# primeiro = 1
# segundo = 2

# range = 3
# elemento = 1+2 =3
# primeiro = 2
# segundo = 3

# range = 4
# elemento = 2+3 = 5
# primeiro = 3
# segundo = 5

# range = 5
# elemento = 3+5 =8
# primeiro = 5
# segundo = 8

# range = 6
# elemento = 5+8 = 13
# primeiro = 8
# segundo = 13

# 1,1,2,3,5,8,13...
