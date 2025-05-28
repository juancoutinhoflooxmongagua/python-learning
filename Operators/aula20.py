
primary_value = input('Digite o primeiro valor :')
secondary_value = input('Digite o segundo valor :')

if primary_value == secondary_value:
    print("Os valores são iguais")
elif primary_value < secondary_value:
    print("O primeiro valor é menor que o segundo")
elif primary_value > secondary_value: 
    print("O primeiro valor é maior que o segundo")
else:
    print('Error')