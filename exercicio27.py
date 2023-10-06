pesoMorango = float(input('Digite o peso de morangos: '))
pesoMaca = float(input('Digite o peso de maçãs: '))
pesoTotal = pesoMaca + pesoMorango
valorTotal = 0
desconto = 0.1
valorDesconto = 0

if pesoMorango < 5:
    precoKiloMorango = 2.5
    valorMorangos = precoKiloMorango*pesoMorango
elif pesoMorango >=5:
    precoKiloMorango = 2.2
    valorMorangos = precoKiloMorango * pesoMorango

if pesoMaca < 5:
    precoKiloMaca = 1.8
    valorMacas = precoKiloMaca*pesoMaca
elif pesoMaca >=5:
    precoKiloMaca = 1.5
    valorMacas = precoKiloMaca* pesoMaca

valorTotal = valorMacas + valorMorangos

if pesoTotal >= 8 or valorTotal >=25:
    valorDesconto = valorTotal*desconto
    valorTotal = valorTotal - valorDesconto

print(f'Valor total: R${valorTotal:.2f}\n'
      f'Desconto: R${valorDesconto:.2f}')