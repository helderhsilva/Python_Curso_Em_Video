from math import fabs

print('---ANÁLISE DE TRIÂNGULO---\n')

a = float(input('1º Segmento = '))
b = float(input('2º Segmento = '))
c = float(input('3º Segmento = '))

# Verificando o segmento a
if (a > fabs(b-c)) and (a < (b+c)) and (b > fabs(a-c)) and (b < (a+c)) and (c > fabs(a-c)) and (c < (a+b)):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmento acima NÃO PODEM FORMAR um triângulo!')

