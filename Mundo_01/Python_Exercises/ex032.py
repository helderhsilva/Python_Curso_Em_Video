from datetime import date

print('---ANO BISSEXTO?---\n')

ano = int(input('Qual ano deseja analisar? Para analisar o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\nO ano {ano} é BISSEXTO')
else:
    print(f'\nO ano {ano} não é BISSEXTO')

