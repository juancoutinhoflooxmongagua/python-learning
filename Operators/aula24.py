name = 'Juan'

print(name[2])

print('Ju' in name)

nome = input('Name:')
find = input('Find: ')


if find in name: 
    print(f'{find} está em {nome}')
else:
    print(f'{find} não está em {nome}')