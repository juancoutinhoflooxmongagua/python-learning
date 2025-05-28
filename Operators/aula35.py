

entry = input('Digite seu nome: ')

name_len = len(entry)

try:
    if name_len <= 4:
        print('Teu nome é Curto')
    elif name_len > 5 or 6:
        print('Teu nome é Normal')
    elif name_len > 6:
        print('Teu nome é muito grande')
except:
    print('ERROR SYSTEM')