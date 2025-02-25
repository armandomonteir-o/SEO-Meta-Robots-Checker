import re

## Função para validar URL


def validate_url(url: str) -> bool:
    """Valida URLs usando regex"""
    pattern = re.compile(
        r"^(https?://)?([A-Z0-9-]+\.)+[A-Z]{2,}(:\d+)?(/[-a-zA-Z0-9@:%_+.~#?&/=]*)?$",
        re.IGNORECASE,
    )
    return bool(pattern.fullmatch(url.strip())) if url else False
