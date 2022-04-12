n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

mean = (n1+n2)/2

print(f'\nSua média é: {mean}')

if mean >= 6:
    print('---Aprovado---')
else:
    print('---Reprovado---')

#print('---Aprovado---' if mean >= 6 else '---Reprovado---')

