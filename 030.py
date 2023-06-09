# Descobrindo se um nomero é par ou impar


digite = int(input("Digite um numero: "))

def parOuImpar(digite):
    
    if digite % 2 == 0:
        print(f"O numero {digite} é par")
    else:
        print(f"O numero {digite} é impar")
    
    
numero = parOuImpar(digite)