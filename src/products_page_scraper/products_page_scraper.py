from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from .product import Product


#Se crea una clase abstracta heredando de ABC
class ProductsPageScraper(ABC):

    #A los metodos le indicamos q es un metodo abstracto decorando con el abstractmethod
    @abstractmethod
    def get_html(self, url: str) -> BeautifulSoup:
        ...

    @abstractmethod
    def get_products(self, html_content: BeautifulSoup) -> list[Product]:
        ...