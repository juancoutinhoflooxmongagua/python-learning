entry = input('Digite a hora em números inteiros: ')

try:
    hora = int(entry)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Hora inválida (deve ser entre 0 e 23)')
except ValueError:
    print('Entrada inválida, digite um número inteiro.')
