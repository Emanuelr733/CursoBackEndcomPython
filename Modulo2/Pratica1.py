class Aluno:
    def __init__(self, nome, curso, matricula):
        self.nome = nome
        self.curso = curso
        self.matricula = matricula

    def apresentar(self):
        mensagem = f"Aluno: {self.nome} | Curso: {self.curso} | Matrícula: {self.matricula}"
        print(mensagem)

    def __str__(self):
        return f"Aluno: {self.nome} | Curso: {self.curso} | Matrícula: {self.matricula}"


aluno1 = Aluno("Emanuel", "Engenharia de Software", "20251001")
aluno2 = Aluno("Maria", "Ciência da Computação", "20251234")
aluno1.apresentar()
aluno2.apresentar()
print(aluno1)
print(aluno2)