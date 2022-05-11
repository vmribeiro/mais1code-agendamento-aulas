from model.Pessoa import Pessoa

class Aula():

    def __init__(self, aluno, professor, horario):
        self.aluno = aluno
        self.professor = professor
        self.horario = horario
    
    def __str__(self):
        string_aula = """\n
        ************************
        Aluno: {aluno}
        Professor: {professor}
        Horario: {horario}
        ************************\n
        """.format(aluno = self.aluno.nome, 
                   professor = self.professor.nome,
                   horario = self.horario)
        return string_aula