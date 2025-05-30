# Bem vindo a consulta de CPF
# 244.430.538-83
cpf = input('Digite seu CPF: ')
cpf_formated = cpf.replace('.', "").replace('-', "")

tuple_cpf = tuple(cpf_formated)

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
    d1 = (sum_total * 10) % 11
    if d1 > 9:
        d1 = 0
    print(f'O primeiro dígito é {d1}')

    # segundo dígito
    n1 = int(tuple_cpf[0]) * 11
    n2 = int(tuple_cpf[1]) * 10
    n3 = int(tuple_cpf[2]) * 9
    n4 = int(tuple_cpf[3]) * 8
    n5 = int(tuple_cpf[4]) * 7
    n6 = int(tuple_cpf[5]) * 6
    n7 = int(tuple_cpf[6]) * 5
    n8 = int(tuple_cpf[7]) * 4
    n9 = int(tuple_cpf[8]) * 3
    n10 = d1 * 2

    sum_total2 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
    d2 = (sum_total2 * 10) % 11
    if d2 > 9:
        d2 = 0
    print(f'O segundo dígito é {d2}')

    cpf_calculado = cpf_formated[:9] + str(d1) + str(d2)

    if cpf_formated == cpf_calculado:
        print('Seu CPF é válido!')
    else:
        print('Seu CPF não é válido!')

sum()
