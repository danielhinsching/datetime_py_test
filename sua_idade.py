from datetime import datetime

def diferenca_anos_meses(data_inicio, data_fim):
    anos = data_fim.year - data_inicio.year
    meses = data_fim.month - data_inicio.month
    dias = data_fim.day - data_inicio.day

    if dias < 0:
        meses -= 1
    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses

nasc_str = input("Digite sua data de nascimento (dd/mm/yyyy): ")
nasc = datetime.strptime(nasc_str, "%d/%m/%Y")
hoje = datetime.now()

anos, meses = diferenca_anos_meses(nasc, hoje)
print(f"Você tem {anos} anos e {meses} meses.")