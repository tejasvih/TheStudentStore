class Product:
    def __init__(self, id, name,category_id,category_name,price,available_quantity,warning_quantity ): 
        self.id = id
        self.name = name
        self.category_name = category_name
        self.category_id = category_id
        self.price = price
        self.available_quantity = available_quantity
        self.warning_quantity = warning_quantity
        