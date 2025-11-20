class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor: Autor):
        self.titulo = titulo
        self.autor = autor   # associação
    def exibir_info(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor.nome}")

autor1 = Autor("Machado de Assis")
livro1 = Livro("Dom Casmurro", autor1)
livro1.exibir_info()

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []   # composição: empresa contém funcionários
    def adicionar_funcionario(self, nome, cargo):
        funcionario = Funcionario(nome, cargo)
        self.funcionarios.append(funcionario)
    def exibir_dados(self):
        print(f"\nEmpresa: {self.nome}")
        print("Funcionários:")
        for f in self.funcionarios:
            print(f"- {f.nome} ({f.cargo})")

empresa = Empresa("Tech Solutions")
empresa.adicionar_funcionario("Emanuel", "Estagiário")
empresa.adicionar_funcionario("Carla", "Gerente de Projetos")
empresa.adicionar_funcionario("Rogério", "Analista de Sistemas")
empresa.exibir_dados()