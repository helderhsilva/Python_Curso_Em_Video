inteiro = int(input('1- Qual tipo primitivo está nesse input? Digite algo: '))
print(f'Nesse input ficou salvo o valor {inteiro}. Ele está trantando o tipo primitivo', type(inteiro))

real = float(input('\n2- Qual tipo primitivo está nesse input? Digite algo: '))
print(f'Nesse input ficou salvo o valor {real}. Ele está trantando o tipo primitivo', type(real))

booleano = bool(input('\n3- Qual tipo primitivo está nesse input? Digite algo: '))
print(f'Nesse input ficou salvo o valor {booleano}. Ele está trantando o tipo primitivo', type(booleano))

text = str(input('\n4- Qual tipo primitivo está nesse input? Digite algo: '))
print(f'Nesse input ficou salvo o valor {text}. Ele está trantando o tipo primitivo', type(text))

whatever = input('\n\nAgora digite qualquer coisa: ')
print(f'\nVocê digitou {whatever}, esse dado é do tipo:', type(whatever))

print(f'\nO dado {whatever} pode ser convertido para um dado alpha-numérico: ', whatever.isalnum())
print(f'O dado {whatever} pode ser convertido para um dado alpha: ', whatever.isalpha())
print(f'O dado {whatever} pode ser convertido para um dado ascii: ', whatever.isascii())
print(f'O dado {whatever} pode ser convertido para um dado dígito: ', whatever.isdigit())
print(f'O dado {whatever} pode ser convertido para um dado lower: ', whatever.islower())
print(f'O dado {whatever} pode ser convertido para um dado decimal: ', whatever.isdecimal())
print(f'O dado {whatever} pode ser convertido para um dado identificador: ', whatever.isidentifier())
print(f'O dado {whatever} pode ser convertido para um dado numérico: ', whatever.isnumeric())
print(f'O dado {whatever} pode ser convertido para um dado imprimível: ', whatever.isprintable())
print(f'O dado {whatever} pode ser convertido para um dado espaço: ', whatever.isspace())
print(f'O dado {whatever} pode ser convertido para um dado título: ', whatever.istitle())
print(f'O dado {whatever} pode ser convertido para um dado supper: ', whatever.isupper())
