#Aqui creamos una clase q contiene la informacion del producto, q lleva los atributos del producto

from dataclasses import dataclass

@dataclass
class Product:

    id: int
    name: str 
    price: str
    url: str 
