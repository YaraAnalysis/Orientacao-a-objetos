class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R$ {:.2f}'.format(self.caixa))
        else:
            print('O valor do caixa está OK. Caixa atual: R$ {:.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    pass

class AgenciaComum(Agencia):
    pass

class AgenciaPremium(Agencia):
    pass


#AgenciaVirtual
agencia_virtual = AgenciaVirtual('99999999', 15246985000, 1000)
agencia_virtual.caixa = 15000
agencia_virtual.verificar_caixa()

#AgenciaPremium
agencia_premium = AgenciaPremium(22225555, 162345987, 1234)
agencia_premium.caixa = 100000
agencia_premium.verificar_caixa()

#Agencia1
agencia1 = Agencia('22223333', 200000000000, 4568)
agencia1.caixa = 1000000
agencia1.verificar_caixa()
agencia1.emprestar_dinheiro(1500, 12345678912, 0.02)
print(agencia1.emprestimos)
agencia1.adicionar_cliente('Yara', 12345678912, 100000)
print(agencia1.clientes)