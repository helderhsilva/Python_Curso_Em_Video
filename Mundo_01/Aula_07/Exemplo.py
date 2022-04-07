#nome = input('Qual é seu nome? ')
#print('Prazer em te conhecer {}!'.format(nome))
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
div_i = n1 // n2
div_r = n1 % n2

print(f' Soma = {soma},\n',
      f'Subtração = {sub},\n',
      f'Multiplicação = {mult},\n',
      'Divisão = {:.3f},\n'.format(div),
      f'Potenciação = {pot},\n',
      f'Divisão Inteira = {div_i},\n',
      f'Resto da Divisão = {div_r}\n')

print(f'Soma = {soma},\nSubtração = {sub},\nMultiplicação = {mult}', end=' ')
print('Divisão = {:.3f}'.format(div))
print(f'Potenciação = {pot}, Divisão Inteira = {div_i}', end=' >>> ')
print(f'Resto da Divisão = {div_r}')
