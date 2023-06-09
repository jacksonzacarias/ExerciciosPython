digite = int(input('Digite um ano: '))


if digite % 4 == 0 and (digite % 100 != 0 or digite % 400 == 0): 
    print(f'O ano {digite} é bissextos')
    
else : 
    print(f'O ano de {digite} não é bissexto ')
    
    