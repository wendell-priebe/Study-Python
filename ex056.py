# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre : 1=a media de idade do grupo
# 2=nome do homem mais velho 3=quantas mulheres tem menos de 20 anos
media = 0
hvelho = 0
hnome = ''
qmulher = 0
for p in range(1, 5):
    nome = str(input('{}º Pessoa, Nome:'.format(p))).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    media += idade
    if p == 1 and sexo in 'Mm':
        hvelho = idade
        hnome = nome
    if sexo in 'Mm' and idade > hvelho:
        hvelho = idade
        hnome = nome
    if idade < 20 and sexo in 'Ff':
        qmulher = qmulher + 1
print('A media de idade do grupo é {} anos'.format(media/4))
print('O Homem mais velho foi {} com {} anos'.format(hnome, hvelho))
print('Tem {} mulheres com menos de 20'.format(qmulher))