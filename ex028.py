#escreva um programa que faça o computador pensar em umprint('\033[30m='*12)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('='*12,'\033[m') numero inteiro de 0 a 5, e peça para o usuario tentar decobrir
#qual foi o numero escolhido pelo computador. o PC deve escrever na tela se o usuario venceu ou perde
from random import randint
from time import sleep
print('-=-'*12)
print('Adivinhe o numero que vou pensar!')
print('-=-'*12)
num = int(input('Digite um numero inteiro de 0 a 5:'))
sorte = randint(0, 5)   #faz o sorteio do numero inteiro
print('PROCESSANDO...')
sleep(2)            #faz o computador dormir por ()segundos
if num == sorte:
    print('PARABENS VOCE ACERTOU = {}'.format(sorte))
else:
    print('Voce nao venceu LOSER')
    print('O numero sorteado foi {}'.format(sorte))