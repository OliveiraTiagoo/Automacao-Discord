import os
import requests
import streamlit as st
from dotenv import load_dotenv

def __main__():
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
                st.error(f'Erro ao enviar a mensagem. Código: {resposta.status_code}')

        except requests.exceptions.RequestException as erro:
            st.error(f'Não foi possivel conectar ao Discord: {erro}')


st.title("Enviar Mensagem para o Discord")
msg = st.text_area("Digite a mensagem para enviar ao Discord:")
msg = msg.strip()

st.button("Enviar", on_click=__main__)