from selenium import webdriver
from products_page_scraper.amazon_products_page_scraper import AmazonProductsPageScraper

def init():
    item = input('Ingrese el nombre del producto a buscar: ')

    #Para usar ChromeOptions debemos tener instalado Google Chrome y tmb necesitamos el driver de Google Chrome
    #El driver se descarga aqui: https://googlechromelabs.github.io/chrome-for-testing/
    options = webdriver.ChromeOptions()

    #Aqui va la ruta donde esta instalado el Google Chrome
    options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

    #Urls de busqueda de amazon y mercadolibre
    amazon_search_result_url = 'https://www.amazon.it/s?k={}'.format(item)
    meli_search_result_url = 'https://listado.mercadolibre.com.ec/{}'.format(item)

    print(amazon_search_result_url, meli_search_result_url)

    #Aqui instanciamos el modelo que creamos para abrir el chrome con la busqueda del producto y obtener el contenido html de la pagina
    amazon_products_page_scraper = AmazonProductsPageScraper(driver=webdriver.Chrome(options=options))
    amazon_search_result_html = amazon_products_page_scraper.get_html(amazon_search_result_url)

    amazon_products = amazon_products_page_scraper.get_products(html_content=amazon_search_result_html)

    #Aqui iteramos la lista que nos da el metodo en amazon_products para mostrarlos al usuario
    for item in amazon_products:
        print('{}. Producto: {}. \nPrecio: ${}'.format(item.id, item.name, item.price), end='\n\n')


if __name__ == '__main__':
    init()