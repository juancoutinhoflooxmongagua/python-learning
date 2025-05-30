
frase = "         SSSSSS PPPPPPP CCCCCC            "

list_frases = frase.split(',')

list_fixed = []

for i, frase in enumerate(list_frases):
    list_frases[i] = list_frases[i].lstrip().rstrip()
    list_fixed = list_frases[i]

print(list_frases)
print(list_fixed)


frases_unidas = '-'.join(list_fixed)

print(frases_unidas)