import os
import requests
import streamlit as st
from dotenv import load_dotenv

def send_message_to_discord(msg):
    load_dotenv()
    
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

    if webhook_url:
        print('Webhook carregado com sucesso!')
    else:
        print('URL do Webhook nao encontrada no .env')

    if not msg:
        st.error('A mensagem não pode estar vazia')
    elif len(msg) > 2000:
        st.error('A mensagem passou o limite de 2000 caracteres')
    else:
        dados = {
            'content': msg
        }
        try:
            resposta = requests.post(webhook_url, json=dados, timeout=10)
            
            if resposta.status_code == 204:
                st.success('Mensagem enviada com sucesso!')
            else:
                logErro('Erro ao enviar a mensagem', f'Código: {resposta.status_code}')

        except requests.exceptions.RequestException as erro:
            logErro('Não foi possivel conectar ao Discord', erro)

def logErro(mensagem, erro):
    st.error(f'{mensagem}: {erro}')
    print(f'{mensagem}: {erro}')

if __name__ == "__main__":
    st.title("Enviar Mensagem para o Discord")
    msg = st.text_area("Digite a mensagem para enviar ao Discord:")
    msg = msg.strip()
    print(msg)

    st.button("Enviar", on_click=send_message_to_discord, args=(msg,))
    