#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se pode ou nao formar um triangulo
print('-=-'*20)
print('Analisando triangulos')
print('-=-'*20)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a<b+c and b<a+c and c<a+b:
    print('Os segmento acima \033[4;30mPODEM FORMAR\033[m triangulos.')
else:
    print('Os segmentos acima \033[31mNAO PODEM FORMAR\033[m triangulos')