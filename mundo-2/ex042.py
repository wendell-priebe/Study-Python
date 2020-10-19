# refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar o tipo de triangulo que sera formado: equilatero=todos lados iglais;
# isosceles = dois lados iguais; escaleno = todos lados diferentes
print('  \033[30m Analisando Triangulos')
a = float(input('Pirmeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
triangulo = a<b+c and b<a+c and c<a+b
if triangulo and a!=b and b!=c and a!=c:
    print('forma um triangulo escaleno.')
elif triangulo and a==b and b==c:
    print('Forma um triangulo equilatero.')
elif triangulo and a==b or b==c or a==c:
    print('Forma um triangulo isosceles.')
else:
    print('Os segmento acima não podem formar um triangulo!')
