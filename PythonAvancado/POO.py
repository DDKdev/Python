class Pessoa:
    pass

pessoa1 = Pessoa()
pessoa2 = Pessoa()

pessoa1.nome = 'Daniel'
pessoa1.idade = 33
pessoa2.nome = 'Ingrid'
pessoa2.idade = 29

print(pessoa1.nome, pessoa2.idade)


# MÉTODO CONSTRUTOR
class Carro:
    def __init__(self, nome, marca, cor):
        self.nome = nome
        self.marca = marca
        self.cor = cor

    def acelerar(self):
        print(f'{self.nome} está acelerando')

    def parar(self):
        print(f'{self.nome} está parando')

carro1 = Carro('Gol','VW', 'Vermelho')
print(carro1.nome, carro1.cor)
carro1.acelerar()
carro1.parar()

