

list = [1, 2, 3, 4]



name = input('Digite seu nome: ')
age = input('Digite sua idade: ')
height = input('Digite sua altura:')
color = input('Digite sua cor')

Person = [name, age, height, color]

print(Person)

def update(name, age, height, color):
    choice = True
    while choice == True : 
            choice = input('Escolha')
            if choice == '1':
                Person[0] = input('Digite seu novo Nome: ')
                print(Person[0])
                update(name, age, height, color)
            elif choice == '2':
                Person[1] = input('Digite Sua nova idade: ')
                print(Person[1])
                update(name, age, height, color)
            elif choice == '3':
                Person[2] = input('Digite sua nova altura: ')
                print(Person[2])
                update(name, age, height, color)
            elif choice == '4':
                Person[3] = input('Digite sua nova cor: ')
                print(Person[3])
                update(name, age, height, color)
            elif choice == '5':
                print(Person)
                update(name, age, height, color)
            else:
                print('Finish')


escolha = input('Deseja atualizar a sua ficha? [Sim]')

format_choices = (escolha)

if format_choices == "sim":
    update(name, age, height, color)
else:
    print(f'Muito obrigado por usar meu sistema {Person[0]}')
