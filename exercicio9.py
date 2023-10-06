num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
num3 = input('Digite outro número: ')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 > num3:
    print(f'{num1}, {num2}, {num3}')
elif num1 > num3 > num2:
    print(f'{num1}, {num3}, {num2}')
elif num2 > num1 > num3:
    print(f'{num2}, {num1}, {num3}')
elif num2 > num3 > num1:
    print(f'{num2}, {num3}, {num1}')
elif num3 > num2 > num1:
    print(f'{num3}, {num2}, {num1}')
elif num3 > num1 > num2:
    print(f'{num3}, {num1}, {num2}')