

# Bem vindo a consulta de CPF

# 244.430.538-83

lista = []

lista = cpf = input('Digite seu CPF: ')
cpf_formated = lista.replace('.', "").replace('-', "")

tuple_cpf = tuple((cpf_formated))

def sum():
    n1 = int(tuple_cpf[0]) * 10

    n2 = int(tuple_cpf[1]) * 9

    n3 = int(tuple_cpf[2]) * 8

    n4 = int(tuple_cpf[3]) * 7

    n5 = int(tuple_cpf[4]) * 6

    n6 = int(tuple_cpf[5]) * 5

    n7 = int(tuple_cpf[6]) * 4

    n8 = int(tuple_cpf[7]) * 3

    n9 = int(tuple_cpf[8]) * 2

    sum_total = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
    
    d1 = sum_total * 10 % 11

    if d1 > 9:
        print('O resultado é zero.')
    else:
        print(f'O resultado é o valor da conta {d1}')
sum()