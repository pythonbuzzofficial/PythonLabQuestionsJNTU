'''
Write a class called Product. The class should have fields called name, amount, 
and price, holding the product’s name, the number of items of that product in stock, 
and the regular price of the product. There should be a method get_price that receives
the number of items to be bought and returns a the cost of buying that many items, 
where the regular price is charged for orders of less than 10 items, a 10% discount 
is applied for orders of between 10 and 99 items, and a 20% discount is applied for orders 
of 100 or more items. There should also be a method called make_purchase that receives the number 
of items to be bought and decreases amount by that much.
'''

class Product:
    def __init__(self,name,amount,price):
        
        self.name = name
        self.amount = amount
        self.price = price
    def get_price(self,quantity):
        
        if quantity < 10:
            discount =0
        elif 10>=quantity<=99:
            discount = 0.10
        else:
            discount = 0.20
        total_price= quantity * self.price *(1-discount)
        return total_price
        
    def make_purchase(self,quantity):
        if quantity>self.amount:
            print("Not enough stock")
            return
        self.amount =self.amount- quantity
        print(f"Purchase successfull ,Remaining stock:{self.amount}")
    
product = Product("Laptop",50,5000)
# print(product.get_price(5))
# print(product.get_price(10))
# print(product.get_price(100))
product.make_purchase(5)
# product.make_purchase(45)
# product.make_purchase(2)
product1 = Product("Phone",100,7000)
# print(product1.get_price(50))
product1.make_purchase(50)


