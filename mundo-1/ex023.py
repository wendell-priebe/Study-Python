#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos gigitos separados
#ex:digite o numero:1834
#unidade:4 - dezena:3 - centena:8 - milhar:1
num = int(input('Digite um numero inteiro de 0 a 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades:{}'.format(u))
print('Dezenas:{}'.format(d))
print('Centanas:{}'.format(c))
print('Milhar:{}'.format(m))

