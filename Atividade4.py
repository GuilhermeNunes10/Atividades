while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print(nome + ", você é menor de idade")
    elif idade >= 18 and idade <= 65:
        print(nome + ", você é adulto")
    else:
        print(nome + ", você é idoso")
    
    continuar = input("Deseja calcular a idade novamente? (sim/não)")
    if continuar.lower() != "sim":
        break

print("Encerrando o programa...")