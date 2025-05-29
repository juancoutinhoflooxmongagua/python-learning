from copy import error


text = iter('Luiz')

print(next(text))


texto = 'Juan'

iterator = iter(texto)

while True:
    try:
        next(iterator)
    except StopIteration:
        break