frase = 'Bora aprender Python '

print('Fatiamento\n')
print(f'1- frase[3] = {frase[3]}')
print(f'2- frase[3:13] = {frase[3:13]}')
print(f'3- frase[13:] = {frase[13:]}')
print(f'4- frase[:13] = {frase[:13]}')
print(f'5- frase[3:13:2] = {frase[3:13:2]}')
print(f'6- frase[3::2] = {frase[3::2]}')
print(f'7- frase[::2] = {frase[::2]}')

print('\nAnálise / Transformação / Divisão / Junção\n')
print('1- frase.count(\'o\') =', frase.count('o'))
print('2- frase.upper() =', frase.upper())
print('3- frase.upper().count(\'O\') =', frase.upper().count('O'))
print(f'4- len(frase) = {len(frase)}')
print(f'5- len(frase.strip()) = {len(frase.strip())}')
print('6- frase.replace(\'aprender\', \'detonar o\') = {}'.format(frase.replace('aprender', 'detonar o')))
print('7- frase.find(\'Aprender\') = {}'.format(frase.find('Aprender')))
print('8- frase.find(\'aprender\') = {}'.format(frase.find('aprender')))
print('9- frase.title().find(\'Aprender\') = {}'.format(frase.title().find('Aprender')))
print('10- \'Bora\' in frase =', 'Bora' in frase)
print(f'11- Divisão - frase.split() = {frase.split()}')
div = frase.split()
print(f'12- div[0] = {div[0]}')
print(f'13- div[1][3] = {div[1][3]}')
print('14- Junção - \' \'.join(div) =', ' '.join(div))


print('\nTeste para escrever texto grande em um print só com """\n')
print("""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
""")
