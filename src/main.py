from selenium import webdriver
from products_page_scraper.amazon_products_page_scraper import AmazonProductsPageScraper
from products_page_scraper.meli_products_page_scraper import MeliProductsPageScraper
from products_page_scraper.product_repository import ProductRepository

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
    contador1 = 0
    for item in amazon_products:
        contador1 +=1
        print('{}. Producto: {}. \nPrecio: ${}'.format(item.id, item.name, item.price), end='\n\n')
        if contador1 == 5:
            break

    #Hacemos que el usuario elija el id del producto que prefiera con un input
    amazon_product_id = input('Ingrese el id del producto de amazon deseado: ')

    for i in amazon_products:
        if amazon_product_id == str(i.id):
            db_amznurl = i.url 
            db_amznprice = i.price
            break

    #Guardamos en una variable el producto elegido de la lista que tiene todos los productos con esta funcion lambda
    amazon_product = next(filter(lambda product: product.id == int(amazon_product_id), amazon_products))



    #Hacemos el mismo proceso pero con los productos de mercado libre
    meli_products_page_scraper = MeliProductsPageScraper(driver=webdriver.Chrome(options=options))
    meli_search_result_html = meli_products_page_scraper.get_html(meli_search_result_url)

    meli_products = meli_products_page_scraper.get_products(html_content=meli_search_result_html)

    contador2 = 0
    for item in meli_products:
        contador2 +=1
        print('{}. Producto: {}. \nPrecio: ${}'.format(item.id, item.name, item.price), end='\n\n')
        if contador2 == 5:
            break

    meli_product_id = input('Ingrese el id del producto de mercado libre deseado: ')

    for i in meli_products:
        if meli_product_id == str(i.id):
            db_meliurl = i.url 
            db_meliprice = i.price
            break

    meli_product = next(filter(lambda product: product.id == int(meli_product_id), meli_products))
    

    #Guardamos los productos elegido en la bbdd
    ProductRepository().save_product(
        name=item,
        amazon_url=str(db_amznurl),
        meli_url=str(db_meliurl),
        amazon_price=str(db_amznprice),
        meli_price=str(db_meliprice)
    )


if __name__ == '__main__':
    init()