nome = str(input('Informe seu nome completo: ')).strip()

print(f'\nAnálise do nome: {nome}')
print(f'Nome apenas com letras maiúsculas: {nome.upper()}')
print(f'Nome apenas com letras minúsculas: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} caractéres.')
print(f'Seu primeiro nome tem {nome.find(" ")} caractéres.')

#
#renameDiv = nome.split()
#renameJoin = ''.join(renameDiv)
#
#print(f'Seu nome tem ao todo {len(renameJoin)} caractéres.')
#print(f'Seu primeiro nome tem {len(renameDiv[0])} caractéres.')
#
