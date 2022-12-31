# Crie um programa que leia o nome completo de uma passoa e mostre:

# O nome com todas as letras maiúsculas
x = "Vida Longa e bela"
print(x.upper())

print("-------------------")

# O nome com todas minusculos.
print(x.lower())
print("-------------------")

# Quantas letras ao (todo Sem considerar espaços)
novafrase = x.replace(' ', '')
print(len(novafrase))

# Quantas letras tem o primeiro nome

dividido = x.split()
qtLetras = dividido[0]
print(len(qtLetras))

