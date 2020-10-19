# desenvolva um programa que leia o primeiro termo e a razao de uma Progressao arritimetica. no final mostre os 10 priemiros termos dessa progressao
print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)
prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = prim + (10-1)* razao
for c in range(prim, dec+razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')