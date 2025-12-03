#Vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# 1. Solicitamos a string (texto)
texto = input("Digite a palavra ou frase: ")

# 2. Solicitamos o número inteiro
# ATENÇÃO: O input() devolve sempre texto, então precisamos converter para int()
repeticies = int(input("Digite o número de vezes para repetir: "))

# 3. A "Mágica" da multiplicação de strings
# O Python entende que Texto * Número = Texto repetido N vezes
resultado = texto * repeticies

# 4. Exibição
print("\n--- Resultado ---")
print(resultado)