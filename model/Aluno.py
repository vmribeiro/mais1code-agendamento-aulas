from model.Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, grau_escolar):
        super().__init__(nome, idade)
        self.grau_escolar = grau_escolar