#faça um programa que leia a largura e a altura de uma parede em metros, calcuele a sua area e a quantidade de tinta
#necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2mquadados
print('Calcular tinta a pintar!')
al = float(input('Altura da parede em metros?'))
la = float(input('Largura da parede em metros?'))
m2 = al * la
tinta = m2 / 2
print('Sua parede tem {}x{} metros e sua area é de {}m².'.format(al,la,m2))
print('Vecê necessita de {} litros de tinta para pintar {:.3f} m².'.format(tinta,m2))