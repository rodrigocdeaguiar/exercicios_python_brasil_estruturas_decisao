import math

valorSaque = input('Digite o valor que deseja sacar: ')
valorSaque = int(valorSaque)


if valorSaque < 10 or valorSaque < 0:
    print('Valor de saque inválido')
elif valorSaque > 100:
    notasCem = math.floor(valorSaque/100)
    resto = valorSaque - (notasCem*100)
    print(f'{notasCem} nota(s) de R$100')
    if resto >= 50:
        notasCinquenta = math.floor(resto/50)
        resto = resto - (notasCinquenta*50)
        print(f'{notasCinquenta} nota(s) de R$50')
    if resto >= 10:
        notasDez = math.floor(resto/10)
        resto = resto - (notasDez*10)
        print(f'{notasDez} nota(s) de R$10')
    if resto >= 5:
        notasCinco = math.floor(resto / 5)
        resto = resto - (notasCinco * 5)
        print(f'{notasCinco} nota(s) de R$5')
    if 0 < resto < 5:
        notasUm = round(resto/1)
        print(f'{notasUm} nota(s) de R$1')
elif 50 <= valorSaque < 100:
    notasCinquenta = math.floor(valorSaque / 50)
    resto = valorSaque - (notasCinquenta * 50)
    print(f'{notasCinquenta} nota(s) de R$50')
    if resto >= 10:
        notasDez = math.floor(resto/10)
        resto = resto - (notasDez*10)
        print(f'{notasDez} nota(s) de R$10')
    if resto >= 5:
        notasCinco = math.floor(resto / 5)
        resto = resto - (notasCinco * 5)
        print(f'{notasCinco} nota(s) de R$5')
    if 0 < resto < 5:
        notasUm = round(resto/1)
        print(f'{notasUm} nota(s) de R$1')
elif 10 <= valorSaque < 50:
    notasDez = math.floor(valorSaque / 10)
    resto = valorSaque - (notasDez * 10)
    print(f'{notasDez} nota(s) de R$10')
    if resto >= 5:
        notasCinco = math.floor(resto / 5)
        resto = resto - (notasCinco * 5)
        print(f'{notasCinco} nota(s) de R$5')
    if 0 < resto < 5:
        notasUm = round(resto/1)
        print(f'{notasUm} nota(s) de R$1')