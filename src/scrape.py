import requests
from parsel import Selector


def scrape(url: str) -> str:
    response = requests.get(url)
    teste = Selector(text=response.text)
    title = teste.css(".product_main h1::text").get()
    price = teste.css(".price_color::text").re_first(r"\d+\.\d{2}")
    description = teste.css("#product_description ~ p::text").get()
    description = description[: -len("...more")]
    image = teste.css(".thumbnail img::attr(src)").get()

    return f"{title}, {price}, {description}, {'http://books.toscrape.com/catalogue/'+image}"
