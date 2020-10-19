# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa . o pragrama vai perguntar o valor da casa, o salario do comprador e em quantos anos
# ele vai pagar. calcule o valor da prestaçao mensal sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado
from math import floor
print('\033[30m Emprestimo imobiliario')
print('-'*24)
nome = str(input('Nome:'))
renda = float(input('Qual a sua renda mensal: R$'))
casa = float(input('Qual o valor da casa? R$'))
parc = float(input('Em quantos anos deseja pagar? '))
qparc = parc * 12
parcelas = floor(qparc)
vparc = casa / qparc
sal = (renda * 30/100)
print('-'*24)
if vparc > sal :
    print('Valor da parcela excedido, não é possivel realizar o emprestimo.')
else:
    print('Emprestimo aceito {}'.format(nome))
print('Valor da parcela R${:.2f}\nMeses de emprestimo {:.0f}'.format(vparc,qparc))
