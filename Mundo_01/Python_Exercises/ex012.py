preco = float(input('Informe o preço atual do produto: R$'))

porcentagem = float(input('Informe quantos % o produto terá de desconto: '))

desconto = 1-(porcentagem/100)

novoPreco = preco * desconto

print(f'O produto que custa R${preco:.2f} com desconto de {porcentagem:.1f}%, passará a custar R${novoPreco:.2f}')
