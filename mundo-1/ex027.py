#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#ex:ana maria de souza 1=ana 2=souza
nome = str(input('Digite seu nome :')).strip().title()
rep = nome.split()
print('Seu primeiro nome é {}'.format(rep[0]))
print('Seu ultimmo nome é {}'.format(rep[len(rep)-1]))
