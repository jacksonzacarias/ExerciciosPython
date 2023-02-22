def infoNumero (numero):
    n = numero.zfill(4)

    if len(n) > 4:
        print("Esse numero é maior que uma milhar")
    else :
            print(f'Unidade: {n[-1]}')
            print(f"Dezena: {n[-2]}")
            print(f"Centena: {n[-3]}")
            print(f"Milhar: {n[-4]}")

def infoMatematica (number):
    n = number

    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10

    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Milhar: {m}')




n = str(input("Digite o numero: "))


print(infoNumero(n))


n = int(n)
print(infoMatematica(n))

















