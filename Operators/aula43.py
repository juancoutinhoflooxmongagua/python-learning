
# Calculadora em Python

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    op = input('Digite um operador')

    valid_number = None
    valid_operators = '+-/*'

    try: 
        n1f = float(n1)
        n2f = float(n2)
        valid_number = True
    except Exception as error:
        print(error)

    if op not in valid_operators:
        print('O operador não é valido')
        continue

    if len(op) > 1:
        print('O operador não é valido')
        continue

    if valid_number is None:
        print('Um ou Ambos números digitados são invalidos')
        continue
    
    if op == '+':
        result = n1f + n2f
    elif op == '-':
        result = n1f - n2f
    elif op == '/':
        result = n1f / n2f
    elif op == '*':
        reuslt = n1f * n2f
    else:
        print(error)

    print(f'A expressão criada foi {n1} {op} {n2} e o resultado é {result}')

    sair = input('Quer sair? [s]').lower().startswith('s')
    print(sair)

    if sair is True:
        break