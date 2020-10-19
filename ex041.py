# a confederaçao nacional de nataçao precisa de um pragrama que leia o ano de nascimento de um atleta e mostra sua ategoria de acordo com a idade
#ate 9 mirim;ate 14 infantil; ate 19 junior; ate 21 senior; acima master
from datetime import date
ano = date.today().year
#nome = str(input('Qual seu nome: '))
nasc = int(input('Ano de nascimento (yyyy): '))
idade = ano - nasc
if (idade>4) and (idade <= 9):
    print('Candidato Mirim, idade: {} anos'.format(idade))
elif idade <=4:
    print('Candidato inapto, sem idade adquada para participar.')
elif (idade>9) and (idade<=14):
    print('Candidato Infantil, idade: {} anos'.format(idade))
elif (idade>14) and (idade<=19):
    print('Candidato Junior, idade {} anos'.format(idade))
elif (idade>19) and (idade<=21):
    print('Candidato Senior, idade {} anos'.format(idade))
else:
    print('Candidato Master, idade {} anos'.format(idade))
