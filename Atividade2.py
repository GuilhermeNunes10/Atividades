meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

resposta = "sim"

while resposta == "sim":
    mes = int(input("Digite um número inteiro entre 1 e 12: "))

    if mes in meses:
        print(meses[mes])
    else:
        print("Mês inválido")

    resposta = input("Quer digitar outro número? (sim/não): ").lower()

print("Encerrando o programa...")