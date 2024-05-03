class Product :
    def __init__(self , name , price , deal_price , rating ) :
        self.name = name
        self.price = price 
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price
    def display_product_details(self) :
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("Savings: {}".format(self.you_save))
    def get_deal_price(self) :
        return self.deal_price 
    
class  ElectronicItem(Product) :
    def __init__(self , name , price , deal_price , rating , warranty_in_months) :
        super().__init__(name , price , deal_price , rating ) 
        self.warranty_in_months =  warranty_in_months
        
    def display_product_details(self) :
        super().display_product_details() 
        print("Warranty {} months".format(self.warranty_in_months ))
        

class GrocerryItem(Product) :
    def __init__(self , name , price , deal_price , rating , expiry_date ) :
        super().__init__(name , price , deal_price , rating ) 
        self.expiry_date = expiry_date
    def display_product_details(self) :
        super().display_product_details() 
        print("Expiry Date: {}".format(self.expiry_date))
        print("")
        

class Order :
    def __init__(self , delivery_speed , delivery_address ) :
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address
        
    def add_items(self , product , quantity) :
        self.items_in_cart.append( ( product , quantity) ) 
        
    def display_order_details(self) :
        for product , quantity in self.items_in_cart :
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("")
            
    def get_total_bill(self): 
        total_bill = 0 
        for product , quantity in self.items_in_cart : 
            price = product.get_deal_price() * quantity 
            total_bill  += price 
        print("Total Bill : {}".format(total_bill ))
        

e =  ElectronicItem("TV" , 20000 , 5000 , 4 , 24)

g = GrocerryItem("Kaju" , 200 , 50 , 4 , "best before 6 months") 


my_order = Order("prime dilevery" , "Hyd")
my_order.add_items( e ,1)
my_order.add_items( g , 5 ) 


my_order.display_order_details()
my_order.get_total_bill()
