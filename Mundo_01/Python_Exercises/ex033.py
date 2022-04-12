print('---MAIOR E MENOR VALOR---\n')

n1 = float(input('Informe o 1º número: '))
n2 = float(input('Informe o 2º número: '))
n3 = float(input('Informe o 3º número: '))

menor = n1
maior = n1

# Verificação do maior
if (n2 > n1) and (n2 > n3):
    maior = n2
elif (n3 > n1) and (n3 > n2):
    maior = n3

# Verificação do menor
if (n2 < n1) and (n2 < n3):
    menor = n2
elif (n3 < n1) and (n3 < n2):
    menor = n3

print(f'\nMaior valor = {maior}')
print(f'Menor valor = {menor}')

