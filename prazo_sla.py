from datetime import datetime, timedelta

def adicionar_dias_uteis(data_inicio, dias):
    data = data_inicio
    adicionados = 0

    while adicionados < dias:
        data += timedelta(days=1)
        if data.weekday() < 5:  
            adicionados += 1
    
    return data

data_str = input("Digite a data de abertura (dd/mm/yyyy HH:MM): ")
sla = int(input("Digite o SLA em dias úteis: "))

data_abertura = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
prazo = adicionar_dias_uteis(data_abertura, sla)

print(f"Data de abertura: {data_abertura}")
print(f"Prazo de SLA: {prazo}")
1