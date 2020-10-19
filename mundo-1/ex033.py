#faça um programa que leia 3 numeros e mostre qual é o mais e qual o menor
print('Ordem numerica')
a = int(input('Digite um numero:'))
b = int(input('Digite outro numero:'))
c = int(input('Digite mais um numero:'))
# verificar menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor numero foi {}'.format(menor))
# verificar maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero foi {}'.format(maior))
