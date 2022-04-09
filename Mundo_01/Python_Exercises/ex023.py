number = int(input('Digite um número de 0 à 9999: '))

number1 = str(number).zfill(4)
#number1 = number1.rjust(4, '0')

print(f'\nUnidade = {number1[3]}')
print(f'Dezena = {number1[2]}')
print(f'Centena = {number1[1]}')
print(f'Milhar = {number1[0]}')

un = (number % 10)
de = (number // 10) % 10
ce = (number // 100) % 10
mi = (number // 1000) % 10

print(f'\nUnidade = {un}')
print(f'Dezena = {de}')
print(f'Centena = {ce}')
print(f'Milhar = {mi}')
