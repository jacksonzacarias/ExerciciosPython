# salario = float(input('Digite o salario do funcionario: '))


# def almento(salario):
#     if salario > 1250: 
#         valor = salario * 0.100  
#         print(f' O seu salario subio R${valor:.2f} e agora você ganha R${salario+valor:,.2f}')  
#     else: 
#         valor = salario * 0.150
#         print(f' O seu salario subio R${valor:.2f} e agora você ganha R${salario+valor,:,.2f}')
        
        
#     return almento

# valor = almento(salario)


def almento(salario):
    if salario > 1250:
        percentual = 0.1
    else:
        percentual = 0.15
    
    valor = salario * percentual
    novo_salario = salario + valor
    
    return valor, novo_salario

salario = float(input('Digite o salário do funcionário: '))

valor_au, novo_salario = almento(salario)

print(f'O seu salário subiu R${valor_au:.2f} e agora você ganha R${novo_salario:,.2f}')
        

    