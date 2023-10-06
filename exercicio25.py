telefonouParaVitima = input('Telefonou para a vítima? SIM ou NÃO? ')
esteveLocalCrime = input('Esteve no local do crime? SIM ou NÃO? ')
moraPertoVitima = input('Mora perto da vítima? SIM ou NÃO? ')
deviaParaVitima = input('Devia para a vítima? SIM ou NÃO? ')
trabalhouComVitima = input('Trabalhava com a vítima? SIM ou NÃO? ')
indicadorCulpabilidade = 0

if telefonouParaVitima.lower() == 'sim':
    indicadorCulpabilidade +=1
else:
    indicadorCulpabilidade += 0

if esteveLocalCrime.lower() == 'sim':
    indicadorCulpabilidade +=1
else:
    indicadorCulpabilidade += 0

if moraPertoVitima.lower() == 'sim':
    indicadorCulpabilidade +=1
else:
    indicadorCulpabilidade += 0

if deviaParaVitima.lower() == 'sim':
    indicadorCulpabilidade +=1
else:
    indicadorCulpabilidade += 0

if trabalhouComVitima.lower() == 'sim':
    indicadorCulpabilidade +=1
else:
    indicadorCulpabilidade += 0

if indicadorCulpabilidade == 2:
    suspeicao = 'Suspeit0'
elif indicadorCulpabilidade == 3 or indicadorCulpabilidade == 4:
    suspeicao = 'Cúmplice'
elif indicadorCulpabilidade == 5:
    suspeicao = 'Assassino'
else:
    suspeicao = 'Inocente'

print(suspeicao)