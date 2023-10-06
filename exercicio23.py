numero = input('Digite um número para análise: ')
numero = float(numero)

if float.is_integer(numero):
    print(f'{numero} é um número inteiro.')
else:
    print(f'{numero} é um número decimal.')