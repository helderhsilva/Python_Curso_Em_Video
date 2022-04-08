from random import sample, shuffle

n1 = input('1º Aluno: ')
n2 = input('2º Aluno: ')
n3 = input('3º Aluno: ')
n4 = input('4º Aluno: ')

lista = [n1, n2, n3, n4]
novaLista1 = sample(lista, k=4)
shuffle(lista)

print(f'A ordem de apresentação será: {novaLista1}')
print(f'A ordem de apresentação será: {lista}')
