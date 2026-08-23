import os
import requests
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

if webhook_url:
    print('Webhook carregado com sucesso!')
else:
    print('URL do Webhook nao encontrada no .env')

msg = input('Digite a mensagem para enviar ao Discord:')
msg = msg.strip()

if not msg:
    print('A mensagem não pode estar vazia')
elif len(msg) > 2000:
    print('A mensagem passou o limite de 2000 caracteres')
else:
    dados = {
        'content': msg
    }
    try:
        resposta = requests.post(webhook_url, json=dados, timeout=10)
        
        if resposta.status_code == 204:
            print ('Mensagem enviada com sucesso!')
        else:
            print('Erro ao enviar a mensagem. Código:{resposta.status_code}')

    except requests.expections.RequestException as erro:
        print(f'Não foi possivel conecetar ao Discord: {erro}')
    