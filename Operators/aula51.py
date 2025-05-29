

secret_key = 'paodemel'
secret_key_len = len(secret_key)
secret_key_len = secret_key_len 
formated = (secret_key_len * 'x')

'''
concat = 'A' + 'B'

print(concat)


x10 = 'x' * 10

print(x10)
'''

digited = None

while secret_key: 
    print(formated)
    digited = input('Digite a letra:')

    if digited in secret_key:
        print('Yes')
        
    else:
        print('no')

