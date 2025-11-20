#-----------Exercicio 1-----------
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    def estudar(self):
        print(f"{self.nome} está estudando {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina}.")

pessoas = [
    Aluno("Emanuel", 20, "Engenharia de Software"),
    Professor("Carla", 40, "Matemática"),
    Aluno("Marcos", 19, "ADS")
]
for p in pessoas:
    p.apresentar()
#-----------Exercicio 2-----------
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria

class CarroEletrico(Veiculo, Eletrico):
    def __init__(self, marca, modelo, bateria):
        Veiculo.__init__(self, marca, modelo)
        Eletrico.__init__(self, bateria)
    def exibir_info(self):
        print(f"{self.marca} {self.modelo} - Bateria: {self.bateria} kWh")

carro = CarroEletrico("Tesla", "Model 3", 75)
carro.exibir_info()
#-----------Exercicio 3-----------
class Pagamento:
    def processar_pagamento(self):
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses.")
        
class PagamentoPix(Pagamento):
    def processar_pagamento(self):
        print("Pagamento via PIX realizado.")

class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        print("Pagamento via Cartão realizado.")

pagamentos = [PagamentoPix(), PagamentoCartao()]
for p in pagamentos:
    p.processar_pagamento()
#-----------Exercicio 4-----------
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

animais = [Cachorro(), Gato()]
for a in animais:
    a.falar()
#-----------Desafio Final-----------
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def calcular_bonus(self):
        raise NotImplementedError("Subclasses devem implementar esse método.")

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05

funcionarios = [
    Gerente("Carla", 8000),
    Estagiario("Emanuel", 1500),
    Gerente("Roberto", 10000)
]
for f in funcionarios:
    print(f"{f.nome} - Bônus: R${f.calcular_bonus():.2f}")