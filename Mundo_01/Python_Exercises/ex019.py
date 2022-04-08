import random

n1 = input('1º Aluno: ')
n2 = input('2º Aluno: ')
n3 = input('3º Aluno: ')
n4 = input('4º Aluno: ')

lista = [n1, n2, n3, n4]

print(f'\nAluno sorteado = {random.choice(lista)}')
