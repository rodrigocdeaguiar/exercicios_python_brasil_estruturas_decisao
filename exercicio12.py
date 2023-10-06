valorHoraTrabalhada = input('Digite o valor da hora/atividade, em R$: ')
horasTrabalhadasMes = input('Digite a quantidade de horas trabalhadas no mês: ')
salarioBruto = float(valorHoraTrabalhada)*int(horasTrabalhadasMes)
descontoInss = salarioBruto*0.1
descontoFgts = salarioBruto*0.11


if salarioBruto<=900:
    descontoIR = 0
    totalDescontos = descontoIR + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f'Salário bruto ({horasTrabalhadasMes}*{valorHoraTrabalhada}): R${salarioBruto}\n'
          f'(-) IR (0%): R${descontoIR}\n'
          f'(-) INSS ( 10%): R${descontoInss}\n'
          f'(-) FGTS (15%): R${descontoFgts}\n'
          f'Total de descontos: R${totalDescontos}\n'
          f'Salário líquido: R${salarioLiquido}')
elif 900 < salarioBruto <= 1500:
    descontoIR = salarioBruto*0.05
    totalDescontos = descontoIR + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f'Salário bruto ({horasTrabalhadasMes}*{valorHoraTrabalhada}): R${salarioBruto}\n'
          f'(-) IR (5%): R${descontoIR}\n'
          f'(-) INSS ( 10%): R${descontoInss}\n'
          f'(-) FGTS (15%): R${descontoFgts}\n'
          f'Total de descontos: R${totalDescontos}\n'
          f'Salário líquido: R${salarioLiquido}')
elif 1500 < salarioBruto <= 2500:
    descontoIR = salarioBruto*0.1
    totalDescontos = descontoIR + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f'Salário bruto ({horasTrabalhadasMes}*{valorHoraTrabalhada}): R${salarioBruto}\n'
          f'(-) IR (10%): R${descontoIR}\n'
          f'(-) INSS ( 10%): R${descontoInss}\n'
          f'(-) FGTS (15%): R${descontoFgts}\n'
          f'Total de descontos: R${totalDescontos}\n'
          f'Salário líquido: R${salarioLiquido}')
elif salarioBruto > 2500:
    descontoIR = salarioBruto * 0.2
    totalDescontos = descontoIR + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f'Salário bruto ({horasTrabalhadasMes}*{valorHoraTrabalhada}): R${salarioBruto}\n'
          f'(-) IR (20%): R${descontoIR}\n'
          f'(-) INSS ( 10%): R${descontoInss}\n'
          f'(-) FGTS (15%): R${descontoFgts}\n'
          f'Total de descontos: R${totalDescontos}\n'
          f'Salário líquido: R${salarioLiquido}')