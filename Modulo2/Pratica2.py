class Conta:
    def __init__(self, titular, saldo=0):
        try:
            self.__titular = titular
            self.__saldo = saldo
        except Exception as e:
            print("Erro ao criar conta:", e)

    @property
    def saldo(self):
        try:
            return self.__saldo
        except Exception as e:
            print("Erro ao acessar saldo:", e)

    @saldo.setter
    def saldo(self, valor):
        try:
            if valor < 0:
                raise ValueError("O saldo não pode ficar negativo!")
            self.__saldo = valor
        except Exception as e:
            print("Erro ao alterar saldo:", e)

    def depositar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O depósito deve ser maior que zero!")
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        except Exception as e:
            print("Erro ao depositar:", e)

    def sacar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O saque deve ser maior que zero!")
            if valor > self.__saldo:
                raise ValueError("Saldo insuficiente para saque!")
            
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        except Exception as e:
            print("Erro ao sacar:", e)

    def mostrar_saldo(self):
        try:
            print(f"Saldo atual de {self.__titular}: R${self.__saldo:.2f}")
        except Exception as e:
            print("Erro ao mostrar saldo:", e)

conta1 = Conta("Emanuel", 1000)
conta2 = Conta("Maria", 500)
conta1.mostrar_saldo()
conta2.mostrar_saldo()
conta1.depositar(300)
conta1.sacar(2000)
conta1.sacar(500)
conta2.depositar(150)
conta2.sacar(50)
conta1.mostrar_saldo()
conta2.mostrar_saldo()