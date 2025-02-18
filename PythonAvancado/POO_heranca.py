# contruir um objeto com base em outro objeto
class Empregado:
    def __init__(self, identificacao, nome):
        self.identificacao = identificacao
        self.nome = nome
    
    def registrarPonto():
        print('Registrando ponto')
    
    def __str__(self):
        return (f'{self.identificacao} do empregado {self.nome}')

empregado1 = Empregado('1212', 'João')
print(empregado1)

#HERANÇA
class CorpoDocente(Empregado):
    def __init__(self, identificacao,nome,disciplina):
        super().__init__(identificacao, nome)
        self.disciplina =disciplina
    
    def registrarNota(self, nota):
        print(f'Nota atribuída: {nota}')
    
professor1 = CorpoDocente('111', 'Angela ribeiro', 'português')
print(professor1.nome)
print(professor1.registrarNota(10))

# class Administrativo
class Administrativo(Empregado):
    def __init__(self, identificacao,nome,cargo):
        super().__init__(identificacao, nome)
        self.cargo = cargo
    
auxiliarAdm = Administrativo('222','Pedro', 'Auxiliar Administrativo')
print(auxiliarAdm.cargo)
