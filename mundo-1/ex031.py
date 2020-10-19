#desenvolva um programa que pergunte a distancia de uma viajem em km; calcule o preço da passagem
# cobrando r$0.50 por km para viajens de ate 200km e r$0.45 para viajens mais longa
km = float(input('Quantos Km tem a viajem?:'))
#if km <=200:
#    print('O valor da passagem ira custar R${:.2f}'.format(km*0.50))
#else:
#    print('O valor da passagem ira custar R${:.2f}'.format(km*0.45))
preço = km *0.50 if km <=200 else km * 0.45
print('O preço da passagem ira custar R${:.2f}'.format(preço))
