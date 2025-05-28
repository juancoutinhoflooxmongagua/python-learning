


name = input("Digite o seu nome: ")
age = input("Digite a sua idade: ")

name_len = len(name)
name_inverted = name[::-1]
first_word = name[0]
last_word = name[-1]

print(f'Seu nome é {name}')
print(f'seu tem {name_len} caracteres')
print(f'Seu nome invertido é {name_inverted}')
print(f'a primeira letra do seu nome é {first_word} e a última é {last_word}')