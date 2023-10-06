numero = input('Digite um número para análise: ')
numero = float(numero)

if numero % 2 == 0:
    parImpar = 'par'
else:
    parImpar = 'ímpar'

if numero > 0:
    maiorMenorZero = 'positivo'
elif numero == 0:
    maiorMenorZero = 'zero'
elif numero < 0:
    maiorMenorZero = 'negativo'

if float.is_integer(numero):
    decimalInteiro = 'inteiro'
else:
    decimalInteiro = 'decimal'

print(f'{numero} é um numero {parImpar}, {maiorMenorZero} e {decimalInteiro}.')