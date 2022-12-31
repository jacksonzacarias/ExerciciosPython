#faça um programa que leia o comprimento do cateto aposto e do cateto oposto de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa é {hipotenusa:.2f}")
