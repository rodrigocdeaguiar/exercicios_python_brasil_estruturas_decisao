tipoCarne = input('Escolha o tipo de carne que o cliente vai levar na promoção:\n'
                  '1 - Filé Duplo\n'
                  '2 - Alcatra\n'
                  '3 - Picanha\n'
                  '\n'
                  '')
qtdeCarne = float(input('Digite a quantidade de carne que o cliente irá levar, em KG: '))
formaPagamento = input('Selecione o método de pagamento:\n'
                  '1 - Cartão Tabajara\n'
                  '2 - Dinheiro\n'
                  '3 - Cartão de débito ou crédito\n'
                  '\n'
                  '')
desconto = 0.05
valorDesconto = 0

if tipoCarne == '1':
    if qtdeCarne < 5:
        precoFileDuplo = 5.8
        valorTotal = precoFileDuplo * qtdeCarne
    elif qtdeCarne >= 5:
        precoFileDuplo = 4.9
        valorTotal = precoFileDuplo * qtdeCarne
elif tipoCarne == '2':
    if qtdeCarne < 5:
        precoAlcatra = 6.8
        valorTotal = precoAlcatra * qtdeCarne
    elif qtdeCarne >= 5:
        precoAlcatra = 5.9
        valorTotal = precoAlcatra * qtdeCarne
elif tipoCarne == '3':
    if qtdeCarne < 5:
        precoPicanha = 7.8
        valorTotal = precoPicanha * qtdeCarne
    elif qtdeCarne >= 5:
        precoPicanha = 6.9
        valorTotal = precoPicanha * qtdeCarne

if formaPagamento == '1':
    valorDesconto = valorTotal * desconto
    valorTotal = valorTotal - valorDesconto

print(f'Valor total: R${valorTotal:.2f}\n'
      f'Valor do desconto: R${valorDesconto:.2f}')