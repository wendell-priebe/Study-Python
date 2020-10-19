#crie um programa que leia um numero inteiro e mostre na tela se é par ou impar
numero = int(input('Digite um numero inteiro:'))
if numero % 2 == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))