class NotaInvalidaError(Exception):
    pass

class Pessoa:
    def __init__(self, nome, cpf, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

class Aluno(Pessoa):
    def __init__(self, nome, cpf, nascimento, matricula, curso):
        super().__init__(nome, cpf, nascimento)
        self.matricula = matricula
        self.curso = curso
        self.notas = []
    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise NotaInvalidaError("A nota deve ser entre 0 e 10.")
        self.notas.append(nota)
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    def situacao(self):
        return "Aprovado" if self.calcular_media() >= 6 else "Reprovado"
    def __str__(self):
        return f"{self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}"

class Professor(Pessoa):
    def __init__(self, nome, cpf, nascimento, salario):
        super().__init__(nome, cpf, nascimento)
        self.salario = salario
    def __str__(self):
        return f"{self.nome} | Salário: R$ {self.salario}"

class Disciplina:
    def __init__(self, nome, carga_horaria, professor: Professor):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor
    def __str__(self):
        return f"{self.nome} | {self.carga_horaria}h | Prof: {self.professor.nome}"

class Turma:
    def __init__(self, nome, disciplina: Disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self.alunos = []
    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)
    def listar_alunos(self):
        if not self.alunos:
            return "Nenhum aluno cadastrado."
        return "\n".join([str(a) for a in self.alunos])
    def __str__(self):
        return f"Turma {self.nome} | Disciplina: {self.disciplina.nome}"