import math

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))

hip1 = ((ca ** 2) + (co ** 2)) ** (1/2)
hip2 = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
hip3 = math.hypot(ca, co)

print(f'\nCateto oposto = {co}')
print(f'Cateto adjacente = {ca}')
print(f'Cálculo 1 da Hipotenusa =  {hip1:.3f}')
print(f'Cálculo 2 da Hipotenusa =  {hip2:.3f}')
print(f'Cálculo 3 da Hipotenusa =  {hip3:.3f}')

