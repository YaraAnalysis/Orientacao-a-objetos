from datetime import datetime
import pytz


class ContaCorrente:

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
        print('Saldo atual: R$ {:,.2f}.'.format(self.saldo))

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


#programa
conta_Yara = ContaCorrente("Yara", "111.222.333.45", '1234', '0001-1')
print(f'=== Nome: {conta_Yara.nome} - Ag: {conta_Yara.agencia} - C/c: {conta_Yara.num_conta}.===')
conta_Yara.depositar(10000)
conta_Yara.sacar(10500)
conta_Yara.consultar_limite()
print('-' * 20)
conta_Yara.consultar_historico_transacoes()
