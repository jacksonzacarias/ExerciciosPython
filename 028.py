import time
from random import randint

numero = randint(0,5)

print(":--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--:\n"
      "Vou pensar em numero entre 0 e 5. e você vai tentar adivinhar!\n"
      ":--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--: ")


ninformado = int(input("Qual foi numero que eu pensei? "))
print("Processando....")

time.sleep(2)
if ninformado == numero:
    print("Parabens você acertou o numero")
else:
    print(f"Infelimente você errou!  O numero que eu pensei é o {numero}")
print("teste")