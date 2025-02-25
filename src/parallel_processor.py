from concurrent.futures import ThreadPoolExecutor, as_completed

## Funções de processamento em paralelo


def process_urls(urls: list, max_workers: int = 5) -> list:
    ## Processa URLs em paralelo
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_single_url, url) for url in urls]
        return [future.result() for future in as_completed(futures)]


def process_single_url(url: str):
    ## Processamento Individual
    from .validator import validate_url
    from .scraper import check_meta_tag

    try:
        if not validate_url(url):
            return {"URL": url, "Status": "URL inválida"}

        status, message = check_meta_tag(url)
        return {"URL": url, "Status": message}

    except Exception as e:
        return {"URL": url, "Status": f"Erro crítico: {str(e)}"}
