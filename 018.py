#faça um programa que lei aum angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
angulo = float(input("Digite o angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem o seno de {seno:.2f}")
print(f"O angulo de {angulo} tem o cosseno de {cosseno:.2f}")
print(f"O angulo de {angulo} tem a tangente de {tangente:.2f}")

