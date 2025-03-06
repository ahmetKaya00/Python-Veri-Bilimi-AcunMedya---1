class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self,quantity):
        if quantity > self.stock:
            print(f"Stok yetersiz! Mevcut Stok: {self.stock}")
            return False
        self.stock -= quantity
        return True
    
    def __str__(self):
        return f"{self.name} - {self.price} TL (Stok: {self.stock})"