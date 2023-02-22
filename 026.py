frase = str(input("Digite uma frase: ")).strip()

print(frase.upper().count("A"))
print(f"A letra (A) aparece a primeira vez na posição: ", frase.upper().find("A"))
print(f"A letra (A) aparece a segunda vez na posição: ", frase.upper().rfind("A"))


