#Faça tres numeros e mostre qual é o maior. 

n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))

def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f'O maior numero é {n1}')
    elif n2 > n1 and n2 > n3:
        print(f'O maior numero é {n2}')
    else:
        print(f'O maior numero é {n3}')
    return maior

def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        print(f'O menor numero é {n1}')
    elif n2 < n1 and n2 < n3:
        print(f'O menor numero é {n2}')
    else:
        print(f'O menor numero é {n3}')
    return menor

numero = maior(n1, n2, n3)
numero = menor(n1, n2, n3)



