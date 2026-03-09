class Product:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_item_value(self):
        return self.price *self.quantity
    

class Inventory:
    def __init__(self):
        self.products=[]

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        if not self.products:
            print(' The inventory is empty ')
            return
        
        print('\n---Actual Inventory---')
        for prod in self.products:
            print(f'Product: {prod.name} / Price: {prod.price} / Quantity: {prod.quantity}')

    def calculate_total_value(self):
        total = sum(prod.get_total_item_value() for prod in self.products)
        return total
        
    

#1.
my_inventory = Inventory()

#2. 
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

#3. we add products to inventory
my_inventory.add_product(product1)
my_inventory.add_product(product2)

#4. we show the total value
total_value = my_inventory.calculate_total_value()
print(f"Valor total del inventario: {total_value}")