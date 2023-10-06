nota1 = input('Digite a nota parcial 1 do aluno: ')
nota2 = input('Digite a nota parcial 2 do aluno: ')
media = (float(nota1)+float(nota2))/2

if 9.0 <= media <= 10:
    print('Conceito: A')
elif 7.5 <= media < 9:
    print('Conceito: B')
elif 6.0 <= media < 7.5:
    print('Conceito: C')
elif 4.0 <= media < 6.0:
    print('Conceito: D')
elif media < 4.0:
    print('Conceito: E')
else:
    print('Valores inválidos!')