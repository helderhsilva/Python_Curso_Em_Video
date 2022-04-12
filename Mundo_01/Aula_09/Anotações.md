# Manipulando Cadeias de Texto

- O que conhecemos por frase, na programação é conhecida por cadeia de caracteres, ou ainda, uma string.
    - Strings são guardadas em espaços de memória e, cada caracter é guardado sequencialmente em um micro espaço 
de memória. Cada caracter guardado recebe um índice.

## Operações com string

> - Fatiamento: "Conseguir pegar pedaços de uma string".
>  - Ex.: Pegar um caracter de uma string guardada em uma variável -> variável[índice].
>  - Ex.: Pegar um conjunto de caracteres em sequência -> variável[começo:fim+1]
>  - Ex.: Pegar um conjunto de caracteres em seguência, mas pulando casas -> variável[começo:fim+1:nPulo]
>  - Ex.: Pegar um conjunto de caracteres começando do início -> variável[:fim+1]
>  - Ex.: Pegar um conjunto de caracteres começando de qualquer ponto até o fim -> variável[começo:]
>  - Ex.: Pegar um conjunto de caracteres começando de qualquer ponto até o fim, pulando casas -> variável[começo::nPulo]

> - Análise: "Tem haver com saber as informações da string, por exemplo, tamanho, letra inicial, letra final, primeira
> palavra inteira".
>  - Ex.: Pegar o comprimento de uma frase -> len(frase)
>  - Ex.: Contar a quantidade de vezes que aparece um caractere -> frase.count('caractere')
>  - Ex.: Contar a quantidade de vezes que aparece um caractere em um fatiamento -> frase.count('caractere', começo, fim+1)
>  - Ex.: Obter o momento em que começa uma determinada sequencia de caracteres -> frase.find('string')
>  - Se passar uma string que não existe dentro da frase para o .find('string'), ele retornará "-1". Isso significa
> que a string não existe e não foi encontrada na frase.
>  - Ex.: Verificar se existe uma string dentro da frase -> 'String' in frase (retorna True ou False)

> - Transformação: "Uma lista de string é imutável. Mas pode ser mudada por meio de métodos".
>  - Ex.: Trocar uma string que existe na frase e substituir por outra string -> frase.replace('String', 'novaString')
>  - Ex.: Colocar todos os caracteres em maiúsculo -> frase.upper()
>  - Ex.: Colocar todos os caracteres em minúsculo -> frase.lower()
>  - Ex.: Colocar todos os caracteres para minúsculo com apenas a primeira letra em maiúsculo -> frase.capitalize()
>  - Ex.: Colocar capitalize palavra por palavra na frase -> frase.title()
>  - Ex.: Remover todos os espaços que não estão sendo usados no começo e no fim da string -> frase.strip()
>  - Ex.: Remover os espaços apenas no lado direito (no fim) -> frase.rstrip()
>  - Ex.: Remover os espaços apenas no lado esquerdo (no começo) -> frase.lstrip()

> - Divisão: "Em tese, serve para dividir uma tring palavra por palavra baseado nos espaços entre elas, de forma a
> serem rearranjados os seus índices"
>  - Ex.: Dividir a string inteira palavra por palavra criando novas listas dentro de uma lista geral -> frase.split()

> - Junção: "O inverso da divisão"
>  - Ex.: Juntar as strings separadas de forma a obter uma string única -> '-'.join(frase)

## Desafios

> 1. Crie um programa que leia o nome completo de uma pessoa e mostre:
>  - O nome com todas as letras maiúsculas;
>  - O nome com todas as letras minúsculas;
>  - Qunatas letras ao todo (sem considerar espaços);
>  - Quantas letras tem o primeiro nome.

> 2. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
> Ex.: Digite um número: 1834
> unidade = 4
> dezena = 3
> centena = 8
> milhar = 1

> 3. Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

> 4. Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

> 5. Faça um programa que leia uma frase pelo teclado e mostre:
>  - Quantas vezes aparece a letra "A";
>  - Em que posição ela aparece a primeira vez;
>  - Em que posição ela aparece a última vez.

> 6. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
> Ex.: Ana Maria de Souza
> primeiro = Ana
> último = Souza