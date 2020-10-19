# crie um programa que leia o ano de nascimento de 7 pessoas. no final mostre quantas pessoas nao atigiram a maioridade e quantas ja sao maiores
# maioridade = 21 anos
from datetime import date
cmaior = 0
cmenor = 0
for c in range(1,8):
    nasc = int(input('{}º Ano de nascimento: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 21:
        cmaior +=1
    else:
        cmenor +=1
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(cmaior))
print('E tambem tivemos {} pessoas MENORES de idade'.format(cmenor))
