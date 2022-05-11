from controller.ControllerAula import ControllerAula

list_aulas = ControllerAula().gerar_base_teste()
professor = ControllerAula().criar_professor(nome = 'Jonas', idade = 35, especialidade = 'Biologia', ativo = False)

print(professor.nome)



#print(aluno.nome)
#print(professor.nome)
#print(list[0].aluno.nome)
#print(list[0].professor.nome)
#print(list[0].horario)