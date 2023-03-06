while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Escolha a operação desejada (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif operacao == '/':
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Operação inválida. Escolha uma das operações básicas (+, -, *, /).")

    continuar = input("Deseja fazer outra operação? (sim/não) ")
    if continuar.lower() != 'sim':
        break

print("Encerrando o programa...")