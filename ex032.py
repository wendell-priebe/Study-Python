#faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
print('Verificaçao de ano bissexto')
ano = int(input('Digite um ano, 0 ira analisar o ano atual:'))
if ano ==0:
    ano = date.today().year                    # date.today().year  biblioteca que pega o ano atua da maquina
if ano%4==0 and ano%100!=0 or ano%400==0:      # != diferente
    print('O ano {} É BISSEXTO'.format(ano))   # == igual
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
