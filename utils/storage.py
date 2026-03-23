import json
import os

CAMINHO = "data/clientes.json"


def carregar_dados():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(CAMINHO):
        return []

    try:
        with open(CAMINHO, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()

            if not conteudo:
                return []

            return json.loads(conteudo)

    except json.JSONDecodeError:
        print("Arquivo JSON corrompido. Reiniciando base.")
        return []


def salvar_dados(dados):
    if not os.path.exists("data"):
        os.makedirs("data")

    with open(CAMINHO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)