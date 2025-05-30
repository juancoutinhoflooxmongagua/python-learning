

# Bem vindo a consulta de CPF

lista = []

cpf = input('Digite seu CPF: ')

lista = cpf

cpf_formated = lista.replace('.', "").replace('-', "")
int_cpf = int(cpf_formated)
list_of_cpf = [int_cpf]
is_int = type(int_cpf)

print(f'CPF FORMATADO PRA INT: {int_cpf}')

# print(is_int)

# INICIANDO

tuple_cpf = tuple((cpf_formated))

def sum():
    n1_cpf = tuple_cpf[0] ; print(f'N1 CPF: {n1_cpf}')
    n1 = int(n1_cpf) * 10
   
    n2_cpf = tuple_cpf[1] ; print(f'N2 CPF: {n2_cpf}')
    n2 = int(n2_cpf) * 9
   
    n3_cpf = tuple_cpf[2] ; print(f'N3 CPF: {n3_cpf}')
    n3 = int(n3_cpf) * 8
   
    n4_cpf = tuple_cpf[3] ; print(f'N4 CPF: {n4_cpf}')
    n4 = int(n4_cpf) * 7
   
    n5_cpf = tuple_cpf[4] ; print(f'N5 CPF: {n5_cpf}')
    n5 = int(n5_cpf) * 6

    n6_cpf = tuple_cpf[5] ; print(f'N6 CPF: {n6_cpf}')
    n6 = int(n6_cpf) * 5
   
    n7_cpf = tuple_cpf[6] ; print(f'N7 CPF: {n7_cpf}')
    n7 = int(n7_cpf) * 4
   
    n8_cpf = tuple_cpf[7] ; print(f'N8 CPF: {n8_cpf}')
    n8 = int(n8_cpf) * 3
   
    n9_cpf = tuple_cpf[8] ; print(f'N9 CPF: {n9_cpf}')
    n9 = int(n9_cpf) * 2
    
    sum_total = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
    
    def_result = sum_total * 10 % 11
    
    print(def_result)

    if def_result > 9:
        print('O resultado é zero.')
    else:
        print('O resultado é o valor da conta')
sum()

# 244.430.538-83