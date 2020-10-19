# crie um programa que leia duas notas de um aluno e calcule sua media, mostrando um mensagem no final de acordo com a media atingida
# reprovado abaixo de 5.0 - recuperaçao 5.0-6.9 - aprovado superior a 7.0
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
if media >=7:
    print('Aluno APROVADO, media: {:.1f}'.format(media))
elif (media>=5) and (media<7):
    print('Aluno em RECUPERAÇÃO, media: {:.1f}'.format(media))
else :
    print('Aluno em REPROVADO, media: {:.1f}'.format(media))
