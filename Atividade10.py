while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    lista_numeros = [num1, num2, num3]
    lista_numeros_ordenada = sorted(lista_numeros)

    print("Os números em ordem crescente são:", lista_numeros_ordenada)

    continuar = input("Deseja ordenar outros números? (sim/não): ")
    if continuar.lower() == "não":
        break