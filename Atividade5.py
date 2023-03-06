while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    media = (num1 + num2 + num3) / 3

    print(f"A média dos números é {media:.2f}")

    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

    continuar = input("Quer tirar sua média novamente? (sim/não) ")
    if continuar.lower() != 'sim':
        break
    
print("Encerrando o programa...")