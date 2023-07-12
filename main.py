from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual

# #programa
# conta_Yara = ContaCorrente("Yara", "111.222.333.45", '1234', '0001-1')
# conta_Zé = ContaCorrente('Beth', '123.456,789-55', '5555', '0002-2')
#
# cartao_Yara = CartaoCredito('Yara', conta_Yara)
# cartao_Zé = CartaoCredito('Zé', conta_Zé)
#
# cartao_Yara.senha = '4321'
# print(cartao_Yara.senha)
#
# print(conta_Yara.__dict__)
# print(cartao_Yara.__dict__)

agencia_premium_especial = AgenciaPremium(22221111, 1588888888888, )
print(agencia_premium_especial.caixa)

'''print(cartao_Yara.titular)
print(cartao_Yara.conta_corrente.num_conta)

print(cartao_Yara.conta_corrente.cartoes[0].numero)
print(cartao_Zé.numero)
print(cartao_Yara.cod_seguranca)
print(cartao_Yara.validade)'''


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