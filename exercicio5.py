nota1 = input('Digite a nota parcial 1 do aluno: ')
nota2 = input('Digite a nota parcial 2 do aluno: ')
media = (float(nota1)+float(nota2))/2

if float(nota1) > 10 or float(nota1) < 0 or float(nota2) > 10 or float(nota2) < 0:
    print('Valores de notas inválidos!')
else:
    if media == 10:
        print('Aprovado com distinção!')
    elif media >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')