# faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade: -se ele vai se alistar ao serviço militar
# -se é a hora de se alistar -se ja passou do tempo do alistamento; seu programa devera mostras o tempo que falta ou que ja passou do prazo
from datetime import date
print('\033[30m   Alistamento Militar')
print('-'*25)
ano = date.today().year
nome = str(input('Qual o seu nome: '))
nasc = int(input('Ano de nascimento (yyyy) : '))
sexo = str(input(' Qual o seu sexo \n [M] = Masculino ou [F] = Feminino\nOpção M ou F :'))
idade = ano - nasc
sex = sexo.upper()
if sex == 'M':
    if idade == 17:
        print('Falta 1 ano para se alistar {}'.format(nome))
        print(' Você deve se alistar em {}'.format(ano+(18-idade)))
    elif idade <18:
        print('Falta {} anos para se alistar {}'.format(18-idade, nome))
        print(' Você deve se alistar em {}'.format(ano+(18-idade)))
    elif idade == 18:
        print('Completa 18 anos esse ano, tem que se alistar {} !'.format(nome))
        print(' Você deve se alistar esse ano de {}'.format(ano))
    elif idade >18:
        print('Já passou {} anos que devia ter se alistado {} !'.format(idade-18, nome))
        print(' Você tem {} anos.\n Seu alistamento foi em {}!'.format(idade,ano+(18-idade)))
    elif idade == 19:
        print('Já passou 1 ano que devia ter se alistado {} !'.format(nome))
        print(' Você tem {} anos.\n Seu alistamento foi em {}!'.format(idade,ano-1))
else:
    print('Alistamento não obrigatorio a mulheres.')