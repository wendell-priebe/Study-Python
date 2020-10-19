#crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
nome = str(input('Qual o seu nome:')).strip()
variavel = 'Silva' in nome.title()
print(variavel)
