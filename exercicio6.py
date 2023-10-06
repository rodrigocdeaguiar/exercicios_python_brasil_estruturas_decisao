num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
num3 = input('Digite outro número: ')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 and num3:
    print(f'{num1} é o maior!')
elif num2 > num1 and num3:
    print(f'{num2} é o maior!')
else:
    print(f'{num3} é o maior!')