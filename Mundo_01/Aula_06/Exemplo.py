n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

soma = n1 + n2

#print(type(n1))
#print('A soma entre', n1, 'e', n2, 'é:', soma)
print('A soma entre {} e {} é: {}'.format(n1, n2, soma))

n3 = input('Digite algo: ')

# Verifica se o que foi digitado pode ser convertido para o tipo informado (no caso alpha-numérico)
print(n3.isalnum())


