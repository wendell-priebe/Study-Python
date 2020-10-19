# crie um programa que faça o computador jogar jokenpo com voce
from random import randint
from time import sleep
jogada = int(input('''Suas opções:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA
Qual é a sua jogada? '''))
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('=-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogada]))
print('-='*11)
if computador == 0:#pedra
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2 :
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Invalida!!!')
elif computador == 1:#papel
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Invalida!!!')
elif computador == 2:#tesoura
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida!!!')
