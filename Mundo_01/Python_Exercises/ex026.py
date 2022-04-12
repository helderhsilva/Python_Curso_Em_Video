frase = str(input('Qual a sua frase favorita? R: ')).strip().upper()

letra = str(input('Informe uma letra para ser feita uma analise: ')).strip().upper()

print('\n Análise da letra na frase.')
print(f'Quantidade de vezes que a letra "{letra}" aparece: {frase.count(letra)}')
print(f'Posição em que aparece pela primeira vez: {frase.find(letra)+1}')
print(f'Posição em que aparece pela última vez: {frase.rfind(letra)}')

