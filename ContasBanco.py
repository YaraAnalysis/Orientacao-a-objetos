from datetime import datetime
import pytz
from random import randint


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
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Saldo atual da conta {}: R$ {:,.2f}.'.format(self._nome, self._saldo))

    def depositar(self, valor):
        print('===DEPÓSITO===')
        print('Depositando R$ {:,.2f}.'.format(valor))
        self._saldo += valor
        self._transacoes.append((valor, 'Saldo: {}'.format(self._saldo), ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        print('===SAQUE===')
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar o valor de R$ {:,.2f}.'.format(valor))
            self.consultar_saldo()
        else:
            self._saldo -= valor
            print('Sacando R$ {:,.2f}. Saldo após o saque: R$ {:,.2f}.'.format(valor, self._saldo))
            self._transacoes.append((-valor, 'Saldo: {}'.format(self._saldo), ContaCorrente._data_hora()))

    def consultar_limite(self):
        print('Limite de cheque especial: R$ {:,.2f}.'. format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('===== Histórico de Transações =====')
        print('== Valor, Saldo, Data e Hora ==')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, 'Saldo: {}'.format(self._saldo), ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, 'Saldo: {}'.format(conta_destino._saldo), ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


#programa
conta_Yara = ContaCorrente("Yara", "111.222.333.45", '1234', '0001-1')
conta_Zé = ContaCorrente('Beth', '123.456,789-55', '5555', '0002-2')

cartao_Yara = CartaoCredito('Yara', conta_Yara)
cartao_Zé = CartaoCredito('Zé', conta_Zé)

print(cartao_Yara.titular)
print(cartao_Yara.conta_corrente._num_conta)

print(cartao_Yara.conta_corrente.cartoes[0].numero)
print(cartao_Zé.numero)
print(cartao_Yara.cod_seguranca)
print(cartao_Yara.validade)


'''
print(f'=== Nome: {conta_Yara._nome} - Ag: {conta_Yara._agencia} - C/c: {conta_Yara._num_conta}.===')
conta_Yara.depositar(10000)
conta_Yara.sacar(500)
conta_Yara.consultar_limite()
print('-' * 20)
conta_Yara.consultar_historico_transacoes()

print('-' * 20)

conta_Yara.transferir(200, conta_Zé)

conta_Yara.consultar_saldo()
conta_Zé.consultar_saldo()

conta_Yara.consultar_historico_transacoes()
conta_Zé.consultar_historico_transacoes() '''