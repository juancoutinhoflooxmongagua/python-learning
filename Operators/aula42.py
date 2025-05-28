name = 'Juan'

tamanho_name = len(name)

indice = 0 
novo_nome = ''

while indice < len(name): 
    letra = name[indice]
    print(letra)
    novo_nome += letra
    indice += 1

print(novo_nome)
