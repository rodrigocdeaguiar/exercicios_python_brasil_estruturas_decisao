nota1 = input('Nota 1: ')
nota2 = input('Nota 2: ')
nota3 = input('Nota 3: ')

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

media = (nota1 + nota2 + nota3)/3

if 7 <= media < 10:
    print(f'Média = {media:.2f}\n'
          f'Resultado: Aprovado')
elif media == 10:
    print(f'Média = {media:.2f}\n'
          f'Resultado: Aprovado com distinção')
elif media < 7:
    print(f'Média = {media:.2f}\n'
          f'Resultado: Reprovado')