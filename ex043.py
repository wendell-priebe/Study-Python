#desenvolva uma logica que leia o peso e a altura e calcule o imc e mostre o status: 18.5=abaixo do peso; 18,5e25=peso ideal; 25-30=sobrepeso;
# 30-40=obesidade; acima de 40=obesidade morbida
peso = float(input('Qual o seu peso em Kg: '))
alt = float(input('Qual a sua altura em Metros: '))
imc = peso/(alt * alt)
if imc <=18.5:
    print('Imc {:.2f} Abaixo do peso.'.format(imc))
elif (imc>18.5)and(imc<=25):
    print('Imc {:.2f} Peso ideal.'.format(imc))
elif (imc>25)and(imc<=30):
    print('Imc {:.2f} Sobrepeso.'.format(imc))
elif (imc>30)and(imc<=40):
    print('Imc {:.2f} Obesidade.'.format(imc))
else:
    print('Imc {:.2f} Obesidade morbida.'.format(imc))
