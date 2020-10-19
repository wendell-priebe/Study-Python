#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'santo'
nome = str(input('Qual o nome da cidade:'))
#variavel = 'santo' in nome.lower()
print(nome[:5].lower() == 'santo')
#print(variavel)