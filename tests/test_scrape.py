from src.scrape import scrape
from tests.expected_description import DESCRIPTION

URL_BASE = "http://books.toscrape.com/catalogue/"
PAGE = "the-grand-design_405/index.html"
IMAGE = "../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg"
TITLE = "The Grand Design"
PRICE = "13.76"
DESCRIPTION = DESCRIPTION.replace("\n", "")


def test_scrape():
    result = scrape(URL_BASE + PAGE)
    assert TITLE in result
    assert URL_BASE + IMAGE in result
    assert PRICE in result
    assert DESCRIPTION in result
