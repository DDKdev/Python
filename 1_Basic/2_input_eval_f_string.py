# média e concatenação
# O input já converte o dado digitado para string, logo, usamos o eval para converter para itneiro
# O f representa o fstring que permite incluir um outro tipo de dado em uma string.
fahrenheit = eval(input('Digite um número: '))
celsius = (5/9) * (fahrenheit-32)
print(f"A conversão resultou em: {celsius}")
