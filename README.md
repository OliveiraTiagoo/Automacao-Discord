# Automação Python → Discord

Uma automação simples em Python que recebe uma mensagem pelo terminal e a envia para um canal do Discord usando um webhook.

## Pré-requisitos

- Python 3
- Uma URL de webhook criada no canal do Discord

## Instalação

No terminal, entre na pasta do projeto e crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as bibliotecas necessárias:

```bash
pip install requests python-dotenv
```

## Configuração do webhook

Crie um arquivo chamado `.env` na raiz do projeto e adicione a URL completa do seu webhook:

```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/SEU_ID/SEU_TOKEN
```

> Nunca publique o arquivo `.env` ou a URL do webhook. Eles permitem enviar mensagens ao seu canal.

## Como executar

Com o ambiente virtual ativado, execute:

```bash
python3 enviar_discord.py
```

Digite uma mensagem no terminal e pressione Enter. O programa valida se o texto está vazio ou excede o limite de 2.000 caracteres do Discord antes de enviá-lo.

## Segurança

O arquivo `.gitignore` deste projeto ignora `.env` e `.venv/`, impedindo que o webhook e as dependências locais sejam enviados ao GitHub.
