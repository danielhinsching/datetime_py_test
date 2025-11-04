from datetime import datetime
from zoneinfo import ZoneInfo

timezone = input("Digite o timezone (ex: America/Sao_Paulo): ")
mensagem = input("Descrição do evento: ")

agora_local = datetime.now(ZoneInfo(timezone))
agora_utc = agora_local.astimezone(ZoneInfo("UTC"))

print(f"[LOCAL] {agora_local.strftime('%d/%m/%Y %H:%M:%S %Z')} - {mensagem}")
print(f"[UTC]   {agora_utc.strftime('%d/%m/%Y %H:%M:%S %Z')}")