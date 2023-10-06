ano = input('Digite o ano em análise, com quatro dígitos: ')
mes = input('Digite o mês em análise, em dígito(s): ')
dia = input('Digite o dia em análise, em dígito(s): ')

if 1 <= len(ano) <= 4:
    ano = int(ano)
    mes = int(mes)
    dia = int(dia)
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if 1 <= dia <= 31:
            print(f'{dia}/{mes}/{ano} é válido!')
        else:
            print('Data inválida!')
    elif mes == 2:
        if 1 <= dia <= 28:
            print(f'{dia}/{mes}/{ano}')
        else:
            print('Data inválida!')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            print(f'{dia}/{mes}/{ano} é válido!')
        else:
            print('Data inválida!')
else:
    print('Data inválida!')