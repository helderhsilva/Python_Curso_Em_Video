dia = int(input('Quantidade de dias pelos quais o automóvel foi alugado: '))
km = float(input('Quilometragem percorrida: '))

precoDia = dia * 60
precoKm = km * 0.15
total = precoKm + precoDia

print(f'\n Valor total a ser pago = R${total:.2f}')
