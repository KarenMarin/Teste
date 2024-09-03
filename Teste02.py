def verifyString(string):
    # Estou convertendo a string para minúscula para facilitar a contagem de 'a' e 'A'
    string_lower = string.lower()

    count_a = string_lower.count('a')
    
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes no seu texto.")
    else:
        print("A letra 'a' não aparece no seu texto.")

texto = input("Digite algo: ")

verifyString(texto)
