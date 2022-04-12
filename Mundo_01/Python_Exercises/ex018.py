from math import sin, cos, tan, radians

angle = float(input('Informe o ângulo: '))

seno = sin(radians(angle))
cosseno = cos(radians(angle))
tangente = tan(radians(angle))

print(f'\nSeno de {angle} = {seno:.3f}')
print(f'Cosseno de {angle} = {cosseno:.3f}')
print(f'Tangente de {angle} = {tangente:.3f}')
