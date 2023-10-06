nome = input('Digite o nome da pessoa: ')
sexo = input('Digite a letra do sexo, conforme: \n'
             'M - Masculino\n'
             'F - Feminino\n'
             '')

if sexo == 'M' or sexo == 'm':
    print(f'Nome: {nome}. Sexo: Masculino.')
elif sexo == 'F' or sexo == 'f':
    print(f'Nome: {nome}. Sexo: Feminino.')
else:
    print('Sexo inválido.')