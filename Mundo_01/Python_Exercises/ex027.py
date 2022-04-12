name = str(input('Nome completo: ')).strip()

print(f'\nNome: {name}')
print(f'Primeiro nome: {name.split()[0]}')
print(f'Último nome: {name.split()[-1]}')

