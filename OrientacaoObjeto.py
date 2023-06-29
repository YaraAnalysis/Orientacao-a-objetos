# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

class TV:
    #cor = 'preta' # significa que todas as classes TV terão o parâmetro cor, só que a cor é fixa em preto.

    def __init__(self, tamanho):
        #self.cor = 'preta'
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f'Canal alterado para {novo_canal}.')


tv_sala = TV(55)
tv_quarto = TV(70)

#tv_sala.cor = 'branca'
TV.cor = 'branca'
print('--COR--')
print(tv_sala.cor)
print(tv_quarto.cor)

print('--TAMANHO--')
print(tv_sala.tamanho)
print(tv_quarto.tamanho)

print('--CANAL--')
tv_sala.mudar_canal('HBOMax')
tv_quarto.mudar_canal('Youtube')
print(tv_sala.canal)
print(tv_quarto.canal)

