while True:
    numero = int(input("Digite um número inteiro: "))

    eh_primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:

            eh_primo = False
            break

    if eh_primo:
        print("O número é primo")
    else:
        print("O número não é primo")

    continuar = input("Deseja digitar outro número? (sim/não) ")
    if continuar.lower() != 'sim':
        break

print("Encerrando o programa...")