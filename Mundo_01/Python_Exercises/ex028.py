from random import randint
from time import sleep

print('\033[33m-=-'*35)
print('\033[34mOlá, eu sou o Computador. Estou pensando em um número entre 0 e 5, será que você consegue adivinhá-lo?')
print('\033[33m-=-'*35)

nComputer = randint(0, 5)
nUser = int(input("\n\033[34mQual número eu pensei? R:"))

if nUser >= 0 and nUser <= 5:

    print('\033[34mPROCESSANDO...')
    sleep(3)

    if nUser == nComputer:
        print(f'\n\033[32mParabéns você acertou. Eu pensei no número {nComputer}')
    else:
        print(f'\n\033[31mQue pena. Eu pensei no número {nComputer} e você disse {nUser}. Mais sorte na próxima')
else:
    print('\n\033[31mVocê é idiota? Eu disse um número entre 0 e 5. Não quero mais brincar com você. Tchau!')
