#escreva um programa que leia a velocidade de um carro; se ele ultrapassar os 80km/h mostre uma mensagem dizendo que ele foi multado
#a multa vai custar r$7.00 por cada km acima do limite
print('Programa de pardal de velocidade limite 80Km/h')
km = int(input('Qual a velocidade:'))
if km <=80:
    print('Voce esta dentro do permitido por lei de 80 Km/h')
else:
    multa = (km - 80) * 7
    print('Voce foi multado por passar a {}Km/h \n em rodovia permitindo maximo 80Km/h em R${:.2f}.'.format(km, multa))