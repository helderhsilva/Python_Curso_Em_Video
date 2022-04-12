print('---RAJUSTE SALARIAL---\n')

salario = float(input('Salário do funcionário: R$'))

if salario > 1250:
    nSalario = salario * 1.10
else:
    nSalario = salario * 1.15

print(f'O novo salário para quem recebe R${salario:.2f} é: R${nSalario:.2f} ')
