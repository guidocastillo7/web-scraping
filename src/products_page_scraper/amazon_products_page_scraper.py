from bs4 import BeautifulSoup

from products_page_scraper.product import Product
from .products_page_scraper import ProductsPageScraper
from time import sleep

class AmazonProductsPageScraper(ProductsPageScraper):

    def __init__(self, driver) -> None:
        self.driver = driver 

    def get_html(self, url: str) -> BeautifulSoup:

        #Este metodo abre el navegador con el url pasado por parametro
        #Como se cierra automaticamente, le ponemos un tiempo de espera con la libreria sleep
        self.driver.get(url)
        sleep(10)

        #Con este metodo extraemos el contenido html de la pagina
        content = self.driver.page_source
        html = BeautifulSoup(content, 'html.parser')

        #Y cerramos el driver
        self.driver.close()

        return html

    

    def get_products(self, html_content: BeautifulSoup) -> list[Product]:
        products: list[Product] = []

        '''Aqui empezamos a buscar los datos de los productos (id, nombre, precio, url) revisando el contenido html
        q enviamos por parametro'''

        #Primero extraemos el div donde esta el producto con todos sus datos
        #Para despues iterarlo y extraer cada dato individualmente
        products_div_list = html_content.find_all('div', {'class':'s-result-item'})

        for index, item in enumerate(products_div_list):
            try:
                item_name = item.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).text

                item_price = item.find('span', {'class':'a-price-whole'}).text \
                    + item.find('span', {'class':'a-price-fraction'}).text
                
                item_url = item.find('a', {'class':'a-link-normal s-no-outline'}).attrs['href']

                #Aqui agregamos cada producto a la lista, q viene de la clase Product q creamos antes
                products.append(Product(id=index+1, name=item_name, price=item_price, url=item_url))


            except Exception as e:
                pass

        return products