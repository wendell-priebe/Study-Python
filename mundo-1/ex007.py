# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua medialuno
a=input('Nome do aluno:')
n1=float(input('Nota materia 1:'))
n2=float(input('Nota materia 2:'))
n3=float(input('Nota materia 3:'))
#m=n1+n2+n3
#mf=m/3
mf=(n1+n2+n3)/3
print('\033[32mO aluno {} tem a media {:.2f} referent as materias 1, 2 e 3.'.format(a, mf))
if mf >= 7:
    print('\033[1;33mO aluno {} PASSOU de ano letivo'.format(a))
else:
    print('\033[31m O aluno {} REPROVOU o ano letivo'.format(a))
