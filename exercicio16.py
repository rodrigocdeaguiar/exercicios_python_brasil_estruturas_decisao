valorASegundoGrau = int(input('Informe o valor inteiro de "A" da equação de segundo grau: '))
valorBSegundoGrau = int(input('Informe o valor inteiro de "B" da equação de segundo grau: '))
valorCSegundoGrau = int(input('Informe o valor inteiro de "C" da equação de segundo grau: '))

if valorASegundoGrau == 0:
    print('Erro! Essa não é uma equação de primeiro grau!')
else:
    delta = valorBSegundoGrau ** 2 - 4 * valorASegundoGrau * valorCSegundoGrau
    if delta < 0:
        print('A equação não possui raízes reais!')
    elif delta == 0:
        xSemLinha = (valorBSegundoGrau * (-1)) / 2 * valorASegundoGrau
        print(f'Essa equação possui apenas uma raíz real.\n'
                      f'x = {xSemLinha}')
    elif delta > 0:
        xLinha = (valorBSegundoGrau * (-1)) + (delta ** 1 / 2) / 2 * valorASegundoGrau
        xDuasLinhas = (valorBSegundoGrau * (-1)) - (delta ** 1 / 2) / 2 * valorASegundoGrau
        print(f'x1 = {xLinha}\n'
              f'x2 = {xDuasLinhas}')