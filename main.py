import pandas as pd
from src.parallel_processor import process_urls


## Função principal


def main():
    # Carrega dados
    df = pd.read_csv("examples/examples.csv")
    urls = df["URLS"].astype(str).tolist()

    resultados = process_urls(urls)

    resultados_ordenados = sorted(resultados, key=lambda x: urls.index(x["URL"]))
    pd.DataFrame(resultados_ordenados).to_excel("examples/output.xlsx", index=False)


if __name__ == "__main__":
    main()
