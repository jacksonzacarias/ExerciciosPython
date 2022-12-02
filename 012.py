#qual é o preço do produto?
p = float(input("Qual é o preço do produto? R$"))
p = p - (p * 5 / 100)
print(f"O produto que custava R${p + (p * 5 / 100):.2f}, na promoção com desconto de 5% vai custar R${p:.2f}")
