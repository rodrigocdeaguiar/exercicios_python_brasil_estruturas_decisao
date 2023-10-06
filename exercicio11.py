salarioAntesAumento = input('Digite o atual salário do funcionário, em R$: ')
salarioAntesAumento = float(salarioAntesAumento)

if salarioAntesAumento <= 280:
    aumentoSalario = salarioAntesAumento*0.2
    percentualReajuste = '20%'
    novoSalario = salarioAntesAumento + aumentoSalario
elif 280 < salarioAntesAumento <= 700:
    aumentoSalario = salarioAntesAumento * 0.15
    percentualReajuste = '15%'
    novoSalario = salarioAntesAumento + aumentoSalario
elif 700 < salarioAntesAumento <= 1500:
    aumentoSalario = salarioAntesAumento * 0.1
    percentualReajuste = '10%'
    novoSalario = salarioAntesAumento + aumentoSalario
elif salarioAntesAumento > 1500:
    aumentoSalario = salarioAntesAumento * 0.05
    percentualReajuste = '5%'
    novoSalario = salarioAntesAumento + aumentoSalario

print(f'Salário antes do reajuste: R${salarioAntesAumento:.2f}\n'
      f'Percentual de reajuste: R${percentualReajuste}\n'
      f'Valor do aumento: R${aumentoSalario:.2f}\n'
      f'Novo salário, após aumento: R${novoSalario:.2f}')