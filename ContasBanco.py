class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print('Saldo atual: R$ {:,.2f}.'.format(self.saldo))

    def depositar(self, valor):
        print('===DEPÓSITO===')
        print('Depositando R$ {:,.2f}.'.format(valor))
        self.saldo += valor

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        print('===SAQUE===')
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar o valor de R$ {:,.2f}.'.format(valor))
            self.consultar_saldo()
        else:
            self.saldo -= valor
            print('Sacando R$ {:,.2f}. Saldo após o saque: R$ {:,.2f}.'.format(valor, self.saldo))

    def consultar_limite(self):
        print('Limite de cheque especial: R$ {:,.2f}.'. format(self._limite_conta()))

#programa
conta_Yara = ContaCorrente("Yara", "111.222.333.45")
conta_Yara.depositar(10000)
conta_Yara.sacar(10500)
conta_Yara.consultar_limite()
