letra = input('Digite uma letra: ')

if len(letra)!=1:
    print('Entrada inválida! Digite uma letra!')
else:
    if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'O' or letra == 'o' or letra == 'u' or letra == 'U':
        print(f'A letra {letra} é uma vogal!')
    else:
        print(f'A letra {letra} é uma consoante!')