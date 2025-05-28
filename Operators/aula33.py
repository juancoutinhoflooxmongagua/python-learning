number = input('Digite um número inteiro: ')

if not number.isdigit():
    print('O valor digitado não é um número inteir')
else:
    num = int(number)
if num % 2 == 0:
    print('O número digitado é par')
else:
    print('O número digitado é impar')