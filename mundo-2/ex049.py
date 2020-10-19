#refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so q agora utilizando um laço
from time import sleep
n = int(input('Digite o numero para ver sua tabuada: '))
for c in range (1, 11):
    print('{} X {:2} = {:2}'.format(n,c,n*c))
    sleep(0.3)
print('='*12)
