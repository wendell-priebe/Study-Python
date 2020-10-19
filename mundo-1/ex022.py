# crie um programa que leia o nome completo de uma pessoa e mostre: 1nome com todas as letras maiusculas
#2nome com todas as letras minusculas 3quantas letras no total sem espaços 4quantas letras tem o primeiro nome
nome=str(input('Digite nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(nome.title())
cont = nome.split()
#cont1 = len(''.join(cont))
#print(cont1)
print(len(nome) - nome.count(' '))
#print(len(cont[0]))
print(nome.find(' '))
print(cont[0], len(cont[0]))
