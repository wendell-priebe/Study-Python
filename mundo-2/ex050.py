#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
 # se o valor digitado for impar desconsidere
s = 0
cont = 0
for c in range (1,7):
    n = int(input('Digite o {}º numero: '.format(c)))
    if n % 2 == 0:
        s = s + n
        cont +=1
print('Voce imformaou {} numeros PARES e a soma foi {}.'.format(cont,s))