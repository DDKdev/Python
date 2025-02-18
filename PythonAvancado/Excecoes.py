#erro de sintaxe SyntaxError

while True:
    try:
        x = int(input('digite um número: '))
        break
    except ValueError as erro:
        print(f'Aconteceu o erro: {erro}')
        # realiza novamente a pergunta e pede para digitar
    except:
        print('Ocorreu um erro inesperado')
print(x)