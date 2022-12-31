def juntar_palavras(lista, delimitador):
    return delimitador.join(lista)


def transMinuscula(nova_frase):
    novafrase = str(nova_frase)

    if novafrase.isupper():
        novo = novafrase.lower()
    else:
        novo = novafrase.lower()
    return novo

def colocando_maiuscula(nova_frase):
    x = str(nova_frase)

    newList = x.split(" ")

    for i in newList:
        novo = transMinuscula(i)
        s = novo[0].upper()
        forma_frase = s + novo[1:]
        newList[newList.index(i)] = forma_frase
    return juntar_palavras(newList, " ")





x = str(input("Digite uma frase:"))
print(colocando_maiuscula(x))


newList = ['viado', 'gay','puta','lesbica']

def transMinusculo(palavra):
    novo = palavra.lower()
    s = novo[0].upper()
    forma_frase = s + novo[1:]
    return forma_frase


palavra = list(map(transMinusculo, newList))
frase = ' '.join(palavra)
print(frase)

# print(str(forma_frase.replace(" ", "")), end=" ")








##print(transMinuscula(newList))











##valor = x.split(" ")








