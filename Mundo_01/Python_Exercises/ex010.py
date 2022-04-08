# Cotação do dólar hoje 07/04/2022 U$1,00 == R$4,75

real = float(input('Quanto de dinheiro você tem na sua carteira? R$'))

dollar = float(input('Qual o valor do dólar hoje? US$'))

buyDollar = real / dollar

print(f'Você pode comprar US${buyDollar:.2f} com R${real:.2f} à um preço de R${dollar:.2f} hoje.')
