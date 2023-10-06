produto1 = input('Digite o nome/marca do primeiro produto: ')
precoProduto1 = input('Digite o preço do primeiro produto: ')
produto2 = input('Digite o nome/marca do segundo produto: ')
precoProduto2 = input('Digite o preço do segundo produto: ')
produto3 = input('Digite o nome/marca do primeiro produto: ')
precoProduto3 = input('Digite o preço do primeiro produto: ')

precoProduto1 = float(precoProduto1)
precoProduto2 = float(precoProduto2)
precoProduto3 = float(precoProduto3)

if precoProduto1 < precoProduto2 < precoProduto3:
    print(f'Você deve comprar o produto {produto1}.')
elif precoProduto1 < precoProduto3 < precoProduto2:
    print(f'Você deve comprar o produto {produto1}.')
elif precoProduto2 < precoProduto1 < precoProduto3:
    print(f'Você deve comprar o produto {produto2}.')
elif precoProduto2 < precoProduto3 < precoProduto1:
    print(f'Você deve comprar o produto {produto2}.')
elif precoProduto3 < precoProduto2 < precoProduto1:
    print(f'Você deve comprar o produto {produto3}.')
elif precoProduto3 < precoProduto1 < precoProduto2:
    print(f'Você deve comprar o produto {produto3}.')