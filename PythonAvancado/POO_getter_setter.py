class Pessoa:
    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def imc(self):
        return (self.peso / (self.altura * self.altura))*10000
    
    #GETTER 
    # @ = decorator
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        self._altura = valor

pessoa1 = Pessoa('Daniel', 100, 33, 174)
pessoa2 = Pessoa('Ingrid', 60, 29, 170)

print(round(pessoa1.imc(),2))
print(round(pessoa2.imc(),2))


