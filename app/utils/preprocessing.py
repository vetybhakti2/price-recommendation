import re

def clean_product_name(name: str) -> str:
    # Remove special characters and trim whitespace
    return re.sub(r"[^a-zA-Z0-9 ]", "", name).strip().lower()