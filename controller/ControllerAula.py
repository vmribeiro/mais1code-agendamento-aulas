from datetime import datetime

from model.Aluno import Aluno
from model.Professor import Professor
from model.Aula import Aula

class ControllerAula():

    def criar_professor(self, nome, idade, especialidade, ativo):
        professor = Professor(nome, idade, especialidade, ativo)
        return professor

    def criar_aluno(self, nome, idade, grau_escolar):
        aluno = Aluno(nome, idade, grau_escolar)
        return aluno

    def agendar_nova_aula(self, aluno, professor, horario):
        return ''

    def gerar_base_teste(self):
        nomes_alunos =  ['Joao', 'Pedro', 'Paula', 'Vanessa']
        idades_alunos = [11, 12, 13, 15]
        graus_escolares_alunos = ['Ensino Fundamental I', 'Ensino Fundamental I', 'Ensino Fundamental II', 'Ensino Fundamental II']

        nomes_professores =  ['Jonas', 'Tiago', 'Victor', 'Paulo']
        idades_professores = [35, 37, 39, 40]
        especialidades_professores = ['Biologia', 'Física', 'Matematica', 'Português']
        ativos_professores = [True, True, False, True]

        list_aulas = []
        for i in range(0, 3):
            aluno = self.criar_aluno(nomes_alunos[i], idades_alunos[i], graus_escolares_alunos[i])
            professor = self.criar_professor(nomes_professores[i], idades_professores[i], especialidades_professores[i], ativos_professores[i])

            aula = Aula(aluno, professor, datetime.strptime('2022-04-22 20:00:00', "%Y-%m-%d %H:%M:%S"))

            list_aulas.append(aula)

        return list_aulas