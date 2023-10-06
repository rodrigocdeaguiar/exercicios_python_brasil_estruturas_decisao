numero = input('Digite um número inferior a 1000: ')

if len(numero) == 1:
    if numero[-1] == '1':
        print(f'{numero} = 1 unidade.')
    else:
        print(f'{numero} = {numero[-1]} unidades')
elif len(numero) == 2:
    if numero[-2] == '1':
        if numero[-1] == '1':
            print(f'{numero} = {numero[-2]} dezena e {numero[-1]} unidade')
        else:
            print(f'{numero} = {numero[-2]} dezena e {numero[-1]} unidades')
    elif numero[-2] != '1':
        if numero[-1] == '1':
            print(f'{numero} = {numero[-2]} dezenas e {numero[-1]} unidade')
        else:
            print(f'{numero} = {numero[-2]} dezenas e {numero[-1]} unidades')
elif len(numero) == 3:
    if numero[-3] == '1':
        if numero[-2] == '1':
            if numero[-1] == '1' or numero[-1] == '0':
                print(f'{numero} = {numero[-3]} centena, {numero[-2]} dezena e {numero[-1]} unidade')
            else:
                print(f'{numero} = {numero[-3]} centena, {numero[-2]} dezena e {numero[-1]} unidades')
        elif numero[-2] != '1':
            if numero[-1] == '1':
                print(f'{numero} = {numero[-3]} centena, {numero[-2]} dezenas e {numero[-1]} unidade')
            else:
                print(f'{numero} = {numero[-3]} centena, {numero[-2]} dezenas e {numero[-1]} unidades')
    elif numero[-3] != '1':
        if numero[-2] == '1':
            if numero[-1] == '1':
                print(f'{numero} = {numero[-3]} centenas, {numero[-2]} dezena e {numero[-1]} unidade')
            else:
                print(f'{numero} = {numero[-3]} centenas, {numero[-2]} dezena e {numero[-1]} unidades')
        elif numero[-2] != '1':
            if numero[-1] == '1':
                print(f'{numero} = {numero[-3]} centenas, {numero[-2]} dezenas e {numero[-1]} unidade')
            else:
                print(f'{numero} = {numero[-3]} centenas, {numero[-2]} dezenas e {numero[-1]} unidades')