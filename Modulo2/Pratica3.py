class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligando de forma genérica...")

class Carro(Veiculo):
    def ligar(self):
        print(f"Carro {self.marca} {self.modelo}: motor ligado com partida elétrica.")

class Moto(Veiculo):
    def ligar(self):
        print(f"Moto {self.marca} {self.modelo}: motor ligado ao girar o pedal.")

class Caminhao(Veiculo):
    def ligar(self):
        print(f"Caminhão {self.marca} {self.modelo}: motor diesel pesado iniciando...")

veiculos = [
    Carro("Toyota", "Corolla"),
    Moto("Honda", "CG 160"),
    Caminhao("Volvo", "FH 540"),
    Carro("Fiat", "Argo"),
    Moto("Yamaha", "Fazer 250")
]

for v in veiculos:
    v.ligar()
