#escreve um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input("Quantos dias alugados? "))
km = float(input("quanto Km rodados? "))

soma = (dia * 60) + (km * 0.15)
print(f"Você alugou o carro por {dia} dias e rodou {km}Km, o total a pagar é R${soma:.2f}")