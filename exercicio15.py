ladoA = input('Digite o valor do lado A do triângulo: ')
ladoB = input('Digite o valor do lado B do triângulo: ')
ladoC = input('Digite o valor do lado C do triângulo: ')

ladoA = float(ladoA)
ladoB = float(ladoB)
ladoC = float(ladoC)

if (abs(ladoB - ladoC) < ladoA < (ladoB + ladoC)) and (abs(ladoA - ladoC) < ladoB < (ladoA + ladoC)) and (abs(ladoA - ladoB) < ladoC) < (ladoA + ladoB):
    if (ladoA == ladoB != ladoC) or (ladoA == ladoC != ladoB) or (ladoB == ladoC != ladoA):
        print('Esse triângulo é isósceles!')
    elif ladoA == ladoB == ladoC:
        print('Esse triângulo é equilátero!')
    elif ladoA != ladoB != ladoC:
        print('Esse triângulo é escaleno!')
else:
    print('Esses valores não correspondem ao de um triângulo!')