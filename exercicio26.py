combustivel = input('Digite o tipo de combustível que deseja abastecer:\n'
                    'A - Álcool\n'
                    'G - Gasolina\n'
                    '\n'
                    '')
litrosCombustivel = float(input('Digite a quantidade de litros que deseja abastacer: '))
litroAlcool = 1.9
litroGasolina = 2.5
valorPagamento = 0

if combustivel.lower() == 'a':
    if litrosCombustivel <= 20:
        litroAlcool = litroAlcool - (litroAlcool*0.03)
        valorPagamento = litrosCombustivel*litroAlcool
    elif litrosCombustivel > 20:
        litroAlcool = litroAlcool - (litroAlcool*0.05)
        valorPagamento = litrosCombustivel*litroAlcool
    else:
        print('Valor inválido!')
elif combustivel.lower() == 'g':
    if litrosCombustivel <= 20:
        litroGasolina = litroGasolina - (litroGasolina*0.03)
        valorPagamento = litrosCombustivel*litroGasolina
    elif litrosCombustivel > 20:
        litroGasolina = litroGasolina - (litroGasolina * 0.05)
        valorPagamento = litrosCombustivel * litroGasolina
    else:
        print('Valor inválido!')
else:
    print('Valor inválido!')

print(f'Valor total: R${valorPagamento:.2f}')