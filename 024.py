cidade = str(input("Digite o nome de uma cidade: ")).strip()

if cidade[:5].upper() == "SANTO":
    print("Essa cidade começa com Santo")
else:
    print(f"A {cidade} não começa com Santo")