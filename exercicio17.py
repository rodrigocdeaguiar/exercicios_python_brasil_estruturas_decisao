ano = input('Digite o ano para saber se o mesmo é bissexto, ou não: ')
ano = int(ano)

if ano < 0:
    print('Dados de entrada inválidos!')
else:
    if ano%4 == 0:
        if ano%100 ==0:
            if ano%400 == 0:
                print('Ano bissexto!')
            else:
                print('Não é ano bissexto!')
        else:
            print('Ano bissexto!')
    else:
        print('Não é ano bissexto!')