# De forma que resutado seje mais legivel

# n = int(input("Digite um número: "))
# print(f"tabuada de {n}: ")
# print(f"{n} x 1 = {n*1}")
# print(f"{n} x 2 = {n*2}")
# print(f"{n} x 3 = {n*3}")
# print(f"{n} x 4 = {n*4}")
# print(f"{n} x 5 = {n*5}")
# print(f"{n} x 6 = {n*6}")
# print(f"{n} x 7 = {n*7}")
# print(f"{n} x 8 = {n*8}")
# print(f"{n} x 9 = {n*9}")
# print(f"{n} x 10 = {n*10}")

# de forma que o resultado seja o mesmo, mas o código seja mais curto.
while True:
    n = int(input("Digite um número: "))
    print(f"tabuada de {n}: ")
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
