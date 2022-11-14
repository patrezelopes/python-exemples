class Cachorro():
    def __init__(self, peso, raca='SRD'):
        self.peso = peso
        self.raca = raca
        self.porte = self.get_porte()

    def get_porte(self):
        if 2 <= self.peso <= 8:
            return 'pequeno'
        elif 8 < self.peso <= 21:
            return 'medio'
        elif 21 < self.peso <= 50:
            return 'grande'
        elif 50 < self.peso <= 80:
            return 'gigante'

    def qtd_racao(self):
        if self.porte == 'pequeno':
            if 2 <= self.peso <= 4:
                qtd_min = 44
                qtd_max = 74
            else:
                qtd_min = 87
                qtd_max = 124
        if self.porte == 'medio':
            if 8 < self.peso <= 14:
                qtd_min = 135
                qtd_max = 188
            else:
                qtd_min = 198
                qtd_max = 255
        if self.porte == 'grande':
            if 21 < self.peso <= 30:
                qtd_min = 264
                qtd_max = 334
            elif 30 < self.peso <= 40:
                qtd_min = 342
                qtd_max = 414
            else:
                qtd_min = 422
                qtd_max = 490
        if self.porte == 'gigante':
            if 50 < self.peso <= 60:
                qtd_min = 497
                qtd_max = 561
            elif 60 < self.peso <= 70:
                qtd_min = 568
                qtd_max = 630
            else:
                qtd_min = 637
                qtd_max = 696

        return f'quantidade diaria para {self.porte} e {self.peso} => minima: {qtd_min}, maxima: {qtd_max}'


peso = int(input('Digite o peso do cachorro: '))
cachorro = Cachorro(peso=peso)
print(cachorro.qtd_racao())

'''
Exemplo de entrada:
Digite o peso do cachorro: 8

exemplode de saída
quantidade diaria para pequeno e 8 => minima: 87, maxima: 124
'''

