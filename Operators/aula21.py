

entry = input('[E]ntrar [S]air')

senha_adm = '1'
senha_digitada = input('Senha: ')

if entry == 'E' and senha_digitada == senha_adm:
    print('Entrou no Sistema')
else: 
    print('Saiu do Sistema')