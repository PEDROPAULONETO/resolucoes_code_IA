#Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

try:
    # Solicita as três notas ao usuário e as converte para float
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcula a média das três notas
    media = (nota1 + nota2 + nota3) / 3

    # Exibe o resultado formatado com duas casas decimais
    print(f"As notas fornecidas foram: {nota1}, {nota2} e {nota3}.")
    print(f"A média final é: {media:.2f}")

except ValueError:
    # Captura o erro se a entrada não for um número válido
    print("Erro: Por favor, digite apenas números válidos para as notas.")
