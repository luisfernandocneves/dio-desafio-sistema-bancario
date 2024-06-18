from abc import ABC, abstractmethod

class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = ""

    @property
    def saldo(self):
        return self.saldo
    
    @property
    def numero(self):
        return self.numero

    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def historico(self):
        return self.historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saque = limite_saques

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    @property
    def endereco(self):
        return self.endereco

    @property
    def contas(self):
        return self.contas

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self.cpf
    
    @property
    def nome(self):
        return self.nome
    
    @property
    def data_nascimento(self):
        return self.data_nascimento

class Historico():
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao(ABC):
    
    @abstractmethod
    def registrar(conta):
        pass

    @property    
    def valor(self):
        return self.valor

class Deposito(Transacao):
    
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.sacar(self.valor)