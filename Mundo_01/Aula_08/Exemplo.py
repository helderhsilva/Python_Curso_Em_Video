#import math                                            # Importação da biblioteca math
from math import sqrt, ceil, floor, trunc               # Importação de funcionalidade da biblioteca math

import random                                           # Importação da biblioteca random

import emoji                                            # Importação da biblioteca emoji

num = int(input('Digite um número: '))

#raiz = math.sqrt(num)                                  # Quando importamos a biblioteca inteira devemos usar o "math."
raiz = sqrt(num)                                        # Quando importamos apenas funcionalidade, basta chamá-las

print(f'Raíz de {num} = {raiz:.2f}')
#
#print(f'Raíz de {num} = {math.ceil(raiz):.2f}')
#print(f'Raíz de {num} = {math.floor(raiz):.2f}')
#print(f'Raíz de {num} = {math.trunc(raiz):.2f}')
#

print(f'Raíz de {num} = {ceil(raiz):.2f}')
print(f'Raíz de {num} = {floor(raiz):.2f}')
print(f'Raíz de {num} = {trunc(raiz):.2f}')

print('\n', '-' * 50, '\n')

rand1 = random.random()
rand2 = random.randint(1, 10)

print(f'Número aleatório usandom random: {rand1:.5f}')
print(f'Número aleatório usando randint: {rand2:.2f}')

print('\n', '-' * 50, '\n')

print(emoji.emojize('Testando emoji no Python :panda_face:', language='alias'))
