velocidade = str(input('Digite a velocidade do carro: '))

def multa_por_velocidade(velocidade):
        x = int(velocidade)
        
        if x >= 81: 
            multa = x * 7
            print('Você ultrapassou a velocidade permitida de 80Km/h..\n'
                    f'Você estava a {velocidade}Km/h\n'
                    f'E vai ser multado em {multa}')
        else:
            print('Parabens continue andando assim')
            
        return multa
    
multa_por_velocidade(velocidade)
    
# if velocidade >= 80: 
#     multa = 7 * velocidade
#     print(f'Você foi multado em {multa}, por que estava a {velocidade}KM/h.')
# else: 
#     print('Parabens continue andando assim')
# 
