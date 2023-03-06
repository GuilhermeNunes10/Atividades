while True:
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    if salario <= 1500:
        aumento = salario * 0.1
    else:
        aumento = salario * 0.05

    novo_salario = salario + aumento
    diferenca = novo_salario - salario

    print(f"Novo salário de {nome}: R$ {novo_salario:.2f} (aumento de R$ {diferenca:.2f})")

    opcao = input("Deseja calcular o novo salário de outro funcionário? (sim/não) ")

    if opcao.lower() == 'não':
        break

print("Encerrando o programa...")