# faça um programa que leia o peso de 5 pessoas. no final mostre qual foi o maior e o menor peso lido
pmaior = 0
pmenor = 0
for p in range(1, 6):
    peso=float(input('{}º Peso em Kg: '.format(p)))
    if p == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print(' O menor peso foi {}Kg'.format(pmenor))
print(' O maior peso foi {}Kg'.format(pmaior))
