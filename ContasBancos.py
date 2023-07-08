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
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Saldo atual da conta {}: R$ {:,.2f}.'.format(self.nome, self._saldo))

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
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property  #método GETTER
    def senha(self):
        return self._senha

    @senha.setter  #método SETTER
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida.")
