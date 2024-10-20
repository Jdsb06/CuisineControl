from file_manager import CustomerManager,MenuManager

class Customer:
    def __init__(self,username=None,password=None):
        self.username=username
        self.password=password
        self.cart=[]
        self.customer_management=CustomerManager()  #for registering new customers, validation
        self.cart_quantities={}
        
    #The below method will be used for the registration of the customer

    def registration(self,username,password):
        self.username=username
        self.password=password
        self.customer_management.customer_registration(username,password)

    #The below method will be used for login

    def login(self,username,password):
        self.username=username
        self.password=password
        return self.customer_management.customer_validation(username,password)

    #The below method will be used to add items to the cart

    def add_item(self,menu,item):
        for i in menu.items:
            if i["Name"]==item:
                self.cart.append(i)

    def sub_item(self, menu, item):
        for i in menu.items:
            if i["Name"] == item:
                self.cart.remove(i)


    def remove_item(self, menu, item_name):
        """Remove all quantities of the item from the cart"""
        self.cart = [i for i in self.cart if i['Name'] != item_name]

    #The below method will be used to view the cart

    def view_cart(self):
        cart={}
        for i in self.cart:
            item=i["Name"]
            if item in cart:
                cart[item]+=1
            else:
                cart[item]=1

        return "\n".join([f'{item} x{number}' for item,number in cart.items()])

    #The below method will be used to find the total amount

    def total_amount(self):
        return round(sum(float(i["Price"]) for i in self.cart), 2)


    #The below method will be used to process payment

    def process_payment(self):
        self.cart = [] #After payment is done, the cart is emptied
        self.cart_quantities={}

class Admin:
    def __init__(self,username="admin",password="admin"):
        self.username=username
        self.password=password

    #Admin validation
    def validate(self,username,password):
        return username==self.username and password==self.password

    #Menu Manager for admin
    def manager(self,menu):
        print("Menu Manager")
        print(menu.display())
