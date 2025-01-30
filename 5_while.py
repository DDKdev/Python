numero = 0
while numero <= 10:
    print(numero)
    numero += 1
print("fim do programa")

# FATORIAL
valor = int(input('Digite um número para calcular o fatorial: '))
fatorial = valor
while valor >= 2:
    fatorial = fatorial * (valor - 1)
    valor -= 1
print(fatorial)
print('Fim do programa')

# Verificando SENHA

senha = '12345'
tentativas = 3
while tentativas != 0:
    tentativa = input("Digite uma senha: ")
    senhaDigitada = tentativa
    if senhaDigitada == senha:
        print('Senha Correta')
        break
    else:
        print('Senha Incorreta')
        tentativas -= 1
