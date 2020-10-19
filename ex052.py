# faça um programa que leia um numero interio e mostre ou nao se é um numero primo
num = int(input('Digite um numero inteiro: '))
tot = 0
for c in range (1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('Numero PRIMO')
else:
    print('Numero NÃO PRIMO')
