#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def verificar_palindromo(texto):
    # 1. Tratamento da string (Limpeza)
    # Removemos espaços em branco e convertemos tudo para minúsculas
    # Isso garante que "Ana" seja igual a "ana"
    texto_limpo = texto.replace(" ", "").lower()

    # 2. Inversão da string (O "Pulo do Gato")
    # No Python, usamos o fatiamento (slicing) [::-1] para inverter
    texto_invertido = texto_limpo[::-1]

    # 3. Comparação
    if texto_limpo == texto_invertido:
        return True
    else:
        return False

# --- Execução do Programa ---
entrada = input("Digite uma palavra ou frase para testar: ")

if verificar_palindromo(entrada):
    print(f"✅ '{entrada}' é um palíndromo!")
else:
    print(f"❌ '{entrada}' não é um palíndromo.")
    print(f"   Lido ao contrário fica: {entrada[::-1]}")