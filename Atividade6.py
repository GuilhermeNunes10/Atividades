resposta = "sim"

while resposta == "sim":
    numero = input("Digite um número inteiro de três dígitos: ")

    if len(numero) != 3:
        print("Número inválido")
    else:
        soma = int(numero[0]) + int(numero[1]) + int(numero[2])
        print("A soma dos dígitos é:", soma)

    resposta = input("Deseja verificar outro número? (sim/não): ").lower()

print("Encerrando o programa...")