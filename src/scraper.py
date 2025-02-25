import requests
from bs4 import BeautifulSoup
from rich import print

## Função para verificar se a meta tag robots está configurada corretamente
## A função retorna uma tupla com o status da verificação e uma mensagem


def check_meta_tag(url: str) -> tuple:
    try:
        headers = {"User-Agent": "SEO Meta Checker/2.0"}

        # Exibe o início do processamento
        print(f"\n🔍 Analisando: {url}\n")

        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code != 200:
            status_msg = f"🚨 ERRO HTTP: {response.status_code}"
            print(f"{status_msg} | URL: {url}\n")
            return (False, status_msg)

        soup = BeautifulSoup(response.text, "html.parser")
        meta_tag = soup.find("meta", attrs={"name": "robots"})

        if not meta_tag:
            status_msg = "⚠️ Meta tag não encontrada"
            print(f"{status_msg} | URL: {url}\n")
            return (False, status_msg)

        content = meta_tag.get("content", "").lower().strip()

        if content == "index, follow":
            status_msg = "✅ Configuração correta: 'index, follow'"
            print(f"{status_msg} | URL: {url}\n")
            return (True, status_msg)
        else:
            status_msg = f"❗Meta Tag encontrada, porém configuração incomum: {content}"
            print(f"{status_msg} | URL: {url}\n")
            return (False, status_msg)

    except Exception as e:
        status_msg = f"🔥 Erro na requisição: {str(e)}"
        print(f"{status_msg} | URL: {url}\n")
        return (False, status_msg)
