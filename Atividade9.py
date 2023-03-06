resposta = "sim"

while resposta == "sim":
    num = int(input("Digite um número inteiro: "))
    soma = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        soma += digit ** 3
        temp //= 10

    if num == soma:
        print(num, "é um número de Armstrong")
    else:
        print(num, "não é um número de Armstrong")

    resposta = input("Deseja verificar outro número? (sim/não): ").lower()

print("Encerrando o programa...")