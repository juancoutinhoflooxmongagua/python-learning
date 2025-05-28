

entry = input('[E]ntrar [S]air')

senha_adm = '1'
senha_digitada = input('Senha: ')

password = senha_digitada or senha_adm  

if (entry == 'E' or 'e') and password:
    print('Entrou no Sistema')
else: 
    print('Saiu do Sistema')