largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print(f'Sua parede tem a dimensão LxA = {largura:.2f}x{altura:.2f}')
print(f'Área da parede = {area} m²')
print(f'Você precisara de {area / 2} litros de tinta para pintar essa parede!')
