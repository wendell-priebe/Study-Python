# faça um programa que leia uma frase pelo teclado e mostre 1quantas veses aparece a letra a
# 2em qual posiçao ela aparece pela primeira vez 3em que posiçao ela aparece a ultima vez
nome = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} veses'.format(nome.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(nome.find('A')+1))
print('A ultima letra A apareceu na posiçao {}'.format(nome.rfind('A')+1))
