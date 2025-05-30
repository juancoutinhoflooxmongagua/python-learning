
list = []

def create(list):
    product = input('Insira o produto desejado: ')
    list.append(product)
    print('Criado com sucesso...')

def delete(list):
    index = input('Digite o índice do produto que deseja apagar: ')
    index_product = int(index)
    
    list.pop(index_product)
    print('Removido com sucesso...')

def order_view():
    print('-----------')

def listing(list):
    list_count = len(list)

    print(f'Lista dos Produtos ( {list_count} )')
    order_view()
    
    for index, item in enumerate(list, start=1):
        print(index, item)    
    order_view()

choice = True
while choice == True:
    menu_choice = input('O que deseja fazer? [I]nserir, [A]pagar, [L]istar: ')
    if menu_choice == 'i':
        create(list)
    elif menu_choice == 'a':
        delete(list)
    elif menu_choice == 'l':
        listing(list)
    else: 
        print('Não identificado')