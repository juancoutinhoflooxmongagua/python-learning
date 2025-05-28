velocidade = 60
local_carro = 100

RADAR_01 = 60
LOCAL_1 = 100
RADAR_RANGE = 1


if local_carro >= LOCAL_1: 
    print('Carro passou no Radar')
    if velocidade > RADAR_01:
        print(f'Carro Multado em Radar 01: Carro na velocidade acima do Permitido: {velocidade}Km/h')
    else:
        print('Velocidade OK')
else:
    print('nada ainda')       

