from model.Pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome, idade, especialidade, ativo):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.ativo = ativo