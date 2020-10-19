#um professor que sortear um do seus 4 alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido
import random
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno:'))
lista = [a, b, c, d]
aluno = random.choice(lista)
print('O aluno escolhido foi {}'.format(aluno))
