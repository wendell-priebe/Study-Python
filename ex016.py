#crie um programa que leio um numero real qualquer e mostre na tela sua porçao inteira
#ex: 6.127 parte inteira = 6
from math import floor, trunc
n = float(input('Digite um numero:'))
#d = floor(n)
#print('O numero inteiro de {} é {}'.format(n,d))
print('O numero inteiro de {} é {}'.format(n,trunc(n)))
