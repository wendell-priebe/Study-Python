#faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 entre 1 ate 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 3 == 0):
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores é {}'.format(cont,soma))
