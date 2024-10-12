import tkinter as tkt
from tkinter import font
from file_manager import OrderManager,CustomerManager,MenuManager


class UI:
    def __init__(self,menu,customer,admin):
        self.menu=menu
        self.customer=customer
        self.admin=admin
        self.order_management=OrderManager()
        self.customer_management=CustomerManager()
        self.root=tkt.Tk()   #Creates the main window
        self.root.title("The Mirch Masala")     #Creates the title
        self.theme()
        """This method has been created so that we don't need to adjust
           format multiple times"""
        self.run()
        """This method has been created so that the application keeps
           running"""

    #The below method is the format which will be followed through the code
    def theme(self):
        self.root.configure(bg="#e6f7ff")
        self.title_font=font.Font(family="Georgia",size=20,weight="bold")
        self.label_font=font.Font(family="Garamond",size=18)
        self.entry_font=font.Font(family="Manhattan",size=18)
        self.button_font=font.Font(family="Consolas",size=16)

    #The below method will clear all the existing UI to prepare for new UI
    def clear_all(self):
        for i in self.root.winfo_children():
            i.destroy()

    #used to ensure that the program keeps running 
    def run(self):
        self.login()
        self.root.mainloop() #used to ensure that the window stays open

    #The below method is used to ensure no pop-ups are there, and UI remains in the same window
    def message(self,message,go_back_to):
        self.clear_all()
        message_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        message_frame.pack()
        
        tkt.Label(message_frame,text=message,bg="#FFFFF0",font=self.label_font).pack()
        tkt.Button(message_frame,text="Got it!",command=go_back_to,font=self.button_font,bg="grey",fg="black").pack()

    #The below method will be used for login UI
    def login(self):
        self.clear_all()
        #frames are used to hold other widgets
        login_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        #padx is for horizontal padding, pady is for vertical padding
        login_frame.pack()
        #this .pack() method calls the login_frame to the window

        #For username
        tkt.Label(login_frame,text="Username",bg="#FFFFF0",font=self.label_font).pack()
        #pack method was not used before in just a single line because it will return None but here it is not an issue
        self.enter_username=tkt.Entry(login_frame,font=self.entry_font)
        #Entry widget is used to accept single line text strings from a user
        self.enter_username.pack(pady=(0,15))
        #padx is taken as (0,0) by default
        #can't add pady in entry widget so add it via pack

        #For password
        tkt.Label(login_frame,text="Password",bg="#FFFFF0",font=self.label_font).pack()
        self.enter_password=tkt.Entry(login_frame,show="*",font=self.entry_font)
        self.enter_password.pack(pady=(0,15))

        #For buttons
        tkt.Button(login_frame,text="Login as Customer",command=self.login_customer,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(login_frame,text="Login as Admin",command=self.login_admin,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(login_frame,text="Registration for New Customers",command=self.register_customer,font=self.button_font,bg="grey",fg="black").pack()

    #used to validate the customer login 
    def login_customer(self):
        username=self.enter_username.get()
        password=self.enter_password.get()
        if self.customer.login(username,password) is True:
            self.customer_window()
        else:
            self.message("Invalid Username or Password.",self.login)

    #used to validate the admin login
    def login_admin(self):
        username=self.enter_username.get()
        password=self.enter_password.get()
        if self.admin.validate(username,password) is True:
            self.admin_window()
        else:
            self.message("Invalid username or Password.",self.login)
        
    #The below UI will be for new customer registration
    def register_customer(self):
        self.clear_all()
        registration_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        registration_frame.pack()

        #For username
        tkt.Label(registration_frame,text="Enter Your Name",bg="#FFFFF0",font=self.label_font).pack()
        self.register_username=tkt.Entry(registration_frame,font=self.entry_font)
        self.register_username.pack(pady=(0,15))

        #For password
        tkt.Label(registration_frame,text="Enter Password",bg="#FFFFF0",font=self.label_font).pack()
        self.register_password=tkt.Entry(registration_frame,show='*',font=self.entry_font)
        self.register_password.pack(pady=(0,15))

        #For buttons
        tkt.Button(registration_frame,text="Register Yourself",command=self.new_customer,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(registration_frame,text="Back to Login Page",command=self.login,font=self.button_font,bg="grey",fg="black").pack()

    #registration logic for new customers
    def new_customer(self):
        username=self.register_username.get()
        password=self.register_password.get()

        #checks for no username/password
        if not username.strip() or not password.strip():
            self.message("Please fill username and password.",self.register_customer)
            return #needs to stop execution
        #checks for same username as other
        if self.customer_management.invalid_username(username):
            self.message("Username not available. Please enter another one.",self.register_customer)
            return

        #valid registration
        self.customer.registration(username,password)
        self.message("You have been Registered. Please login to proceed",self.login)

    #The main page for customer UI
    def customer_window(self):
        self.clear_all()
        main_customer_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        main_customer_frame.pack()

        tkt.Label(main_customer_frame,text=f'Greetings! {self.customer.username}',bg="#FFFFF0",font=self.title_font).pack()
        tkt.Label(main_customer_frame,text="Today's Menu",bg="#FFFFF0",font=self.label_font).pack()
        tkt.Label(main_customer_frame,text=self.menu.display(),bg="#f2f2f2",font=self.label_font).pack()
        tkt.Label(main_customer_frame,text="What item would you wish to order?(Enter as written in Menu)",bg="FFFFF0",font=self.label_font).pack()

        #item to be ordered
        cart_item=tkt.Entry(main_customer_frame,font=self.entry_font)
        cart_item.pack(pady=(0,15))

        #quantity to be ordered
        cart_item_quantity=tkt.Entry(main_customer_frame,font=self.entry_font)
        cart_item_quantity.pack(pady=(0,15))

        #Buttons
        tkt.Button(main_customer_frame,text="Add item to Cart",command=self.add_to_cart,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="View Cart",command=self.view_cart,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Remove item from Cart",command=self.remove_from_cart,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Order History",command=self.order_history,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Place Order",command=self.place_order,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Logout",command=self.logout,font=self.button_font,bg="grey",fg="black").pack()
    
              
    def add_to_cart(self):
        pass
    def view_cart(self):
        pass
    def remove_from_cart(self):
        pass
    def order_history(self):
        pass
    def place_order(self):
        pass
    def logout(self):
        pass
        
        
    def admin_window(self):
        pass
    
        
        
            
    
        

        
        
        
            
        
