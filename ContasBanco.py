from datetime import datetime
import pytz


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome: Nome do Cliente
        cpf: CPF do Cliente. Deve ser inserido com pontos e traços
        agencia: Agencia responsável pela conta do Cliente
        num_conta: Número da Conta Corrente do Cliente
        saldo: Saldo disponível na conta do Cliente
        limite: Limite do cheque especial daquele cliente
        transacoes: Histórico de Transações do Cliente

    Métodos:

    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Saldo atual da conta {}: R$ {:,.2f}.'.format(self.nome, self.saldo))

    def depositar(self, valor):
        print('===DEPÓSITO===')
        print('Depositando R$ {:,.2f}.'.format(valor))
        self.saldo += valor
        self.transacoes.append((valor, 'Saldo: {}'.format(self.saldo), ContaCorrente._data_hora()))

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
            self.transacoes.append((-valor, 'Saldo: {}'.format(self.saldo), ContaCorrente._data_hora()))

    def consultar_limite(self):
        print('Limite de cheque especial: R$ {:,.2f}.'. format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('===== Histórico de Transações =====')
        print('== Valor, Saldo, Data e Hora ==')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, 'Saldo: {}'.format(self.saldo), ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, 'Saldo: {}'.format(conta_destino.saldo), ContaCorrente._data_hora()))


#programa
conta_Yara = ContaCorrente("Yara", "111.222.333.45", '1234', '0001-1')
print(f'=== Nome: {conta_Yara.nome} - Ag: {conta_Yara.agencia} - C/c: {conta_Yara.num_conta}.===')
conta_Yara.depositar(10000)
conta_Yara.sacar(500)
conta_Yara.consultar_limite()
print('-' * 20)
conta_Yara.consultar_historico_transacoes()

print('-' * 20)
conta_maeLira = ContaCorrente('Beth', '123.456,789-55', '5555', '0002-2')
conta_Yara.transferir(200, conta_maeLira)

conta_Yara.consultar_saldo()
conta_maeLira.consultar_saldo()

conta_Yara.consultar_historico_transacoes()
conta_maeLira.consultar_historico_transacoes()

help(ContaCorrente)
