print('---CALCULADORA DE PASSAGEM---\n')

distancia = float(input('Qual a distância da viagem em km? '))

#preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print(f'Para uma viagem de {distancia:.2f} km, o valor da passagem será de R${valor:.2f}')
