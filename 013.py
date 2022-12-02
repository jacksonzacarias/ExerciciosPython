#qual salario do funcionario?
s = float(input("Qual salario do funcionario? R$"))
d = s + (s * 15 / 100)
print(f"Um funcionario que ganhava R${s}, com 15% de aumento, passa a receber R${d:.2f}")
