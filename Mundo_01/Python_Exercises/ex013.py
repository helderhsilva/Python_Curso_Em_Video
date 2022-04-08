salario = float(input('Salário do funcionário: R$'))

porcentagem = float(input('Quantos % será o aumento do salário? '))

aumento = 1 + (porcentagem/100)

novoSalario = salario * aumento

print(f'O salário atual do funcionário é de R${salario:.2f} - Com um aumento de {porcentagem:.1f}%,',
      f'o novo salário será de R${novoSalario:.2f}')
