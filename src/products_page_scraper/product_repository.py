import sqlite3

#Creamos el modelo para la conexion de la base de datos y guardar los productos
class ProductRepository:

    def __init__(self):
        self.client = sqlite3.connect('web-scraping')

        self.db = self.client.cursor()


    def save_product(self, name: str, amazon_url: str, meli_url: str, amazon_price: str, meli_price: str):
        self.db.execute('''
            INSERT INTO product (name, amazon_url, meli_url, amazon_price, meli_price)
            VALUES (?, ?, ?, ?, ?)
            ''', (name, amazon_url, meli_url, amazon_price, meli_price))
        
        self.client.commit()