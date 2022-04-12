print('---RADAR---\n')

velocidade = float(input('Velocidade atual do carro em km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Limite de 80 km/h excedido.')
    print(f'Carro multado. Valor da multa = R${multa:.2f}')
else:
    print('Velocidade dentro do limite.')
