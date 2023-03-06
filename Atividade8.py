resposta = "sim"

while resposta == "sim":
    idade = int(input("Digite a idade da pessoa: "))
    cigarros_por_dia = int(input("Digite a quantidade de cigarros que ela fuma por dia: "))

    total_cigarros = cigarros_por_dia * 365 * idade
    dias_perdidos = (total_cigarros * 10) / (24 * 60)

    print(f"A pessoa perdeu {dias_perdidos:.2f} dias de vida devido ao hábito de fumar.")

    resposta = input("Deseja calcular o número de dias perdidos para outra pessoa? (sim/não): ").lower()

print("Encerrando o programa...")