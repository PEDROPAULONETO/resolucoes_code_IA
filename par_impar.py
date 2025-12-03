#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

try:
    # Solicita um número inteiro como entrada
    numero = int(input("Digite um número inteiro: "))

    # Utiliza uma expressão condicional para verificar se é par ou ímpar
    # Se o resto da divisão por 2 for 0, o número é 'par', senão é 'ímpar'.
    resultado = "par" if numero % 2 == 0 else "ímpar"

    # Exibe o resultado de forma clara
    print(f"O número {numero} é {resultado}.")

except ValueError:
    # Captura o erro se a entrada não for um número inteiro válido
    print("Erro: Por favor, digite um número inteiro válido.")
