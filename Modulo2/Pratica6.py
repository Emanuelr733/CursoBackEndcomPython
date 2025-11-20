# Exceção personalizada
class NotaInvalidaError(Exception):
    def __init__(self, nota, mensagem="Nota inválida! A nota deve estar entre 0 e 10."):
        super().__init__(mensagem)
        self.nota = nota

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.nota = None
    def definir_nota(self, nota):
        try:
            if nota < 0 or nota > 10:
                raise NotaInvalidaError(nota)
            self.nota = nota
            print(f"Nota definida com sucesso para {self.nome}: {self.nota}")
        except NotaInvalidaError as e:
            print(f"Erro ao definir a nota para {self.nome}: {e}")

aluno1 = Aluno("Emanuel")
aluno1.definir_nota(8)
aluno1.definir_nota(15)