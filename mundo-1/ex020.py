#o mesmo professor quer soterar a ordem de apresentaçao dos tabalho dos alunos,
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno:'))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)

  #random.shuffle embaralha a lista