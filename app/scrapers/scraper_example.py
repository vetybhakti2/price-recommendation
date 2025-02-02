import requests
from bs4 import BeautifulSoup

def scrape_product_prices(url: str) -> list[dict]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    # Parsing logic here
    for product_element in soup.select(".product-item"):
        name = product_element.select_one(".product-name").get_text(strip=True)
        price = product_element.select_one(".product-price").get_text(strip=True)
        products.append({"product_name": name, "price": price})

    return products