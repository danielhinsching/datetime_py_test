from datetime import datetime, timedelta

inicio_str = input("Digite a data de início da assinatura (dd/mm/yyyy): ")
duracao = int(input("Digite a quantidade de dias da assinatura: "))

data_inicio = datetime.strptime(inicio_str, "%d/%m/%Y")
data_fim = data_inicio + timedelta(days=duracao)
hoje = datetime.now()

if hoje <= data_fim:
    dias_restantes = (data_fim - hoje).days
    print(f"Assinatura ativa. Dias restantes: {dias_restantes}")
else:
    print("Assinatura expirada.")