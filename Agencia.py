from random import randint

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

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000
    pass


#AgenciaVirtual
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, 142365987)
agencia_virtual.verificar_caixa()
#print(agencia_virtual.site)

#AgenciaComum
agencia_comum = AgenciaComum(22225555, 255000000000)
#agencia_comum.verificar_caixa()

#AgenciaPremium
agencia_premium = AgenciaPremium(22225555, 162345987)
#agencia_premium.verificar_caixa()

agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)


'''#Agencia1
agencia1 = Agencia('22223333', 200000000000, 4568)
agencia1.caixa = 1000000
agencia1.verificar_caixa()
agencia1.emprestar_dinheiro(1500, 12345678912, 0.02)
print(agencia1.emprestimos)
agencia1.adicionar_cliente('Yara', 12345678912, 100000)
print(agencia1.clientes)'''