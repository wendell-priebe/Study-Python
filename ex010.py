# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar
#considerar us$1,00=R$3,27
print('\033[30mConversor Real x Dolar')
n=float(input('Quantos reais você tem ?R$'))
d=n/3.85
print('Você pode comprar US${:.2f} dolares com R$ {:.2f} reais'.format(d,n))
if n >= 1000:
    print('Ou você pode investir em ações ou investimentos que geram juros.')