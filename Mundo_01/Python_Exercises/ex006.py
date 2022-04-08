number = int(input('Digite um número: '))

#
#dobro = number * 2
#triplo = number * 3
#raiz = number ** (1/2)
#
#print(f'\nNúmero digitado: {number}')
#print(f'Dobro de {number} = {dobro}')
#print(f'Triplo de {number} = {triplo}')
#print('Raiz quadrada de {} = {:.2f}'.format(number, raiz))
#

print(f'\nNúmero digitado: {number}')
print(f'Dobro de {number} = {number * 2}')
print(f'Triplo de {number} = {number * 3}')
print('Raiz quadrada de {} = {:.2f}'.format(number, pow(number, (1/2))))
