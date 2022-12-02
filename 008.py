# escrever um programa que converte metros para centimetros e milimetros e outros

n = float(input("Digite um valor em metros: "))
print(f"{n} metros é igual a {n * 100} centimetros,"
      f"\n {n * 1000} milimetros, "
      f"\n {n * 100}hm  "
      f"{n * 10000}dam \n "
      f"{n * 10}dm \n {n * 100}cm "
      f"\n {n * 1000}mm")
