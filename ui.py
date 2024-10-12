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
        
        tkt.Label(message_frame,text=message,bg="#fffff0",font=self.label_font).pack()
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
        tkt.Label(login_frame,text="Username",bg="#fffff0",font=self.label_font).pack()
        #pack method was not used before in just a single line because it will return None but here it is not an issue
        self.enter_username=tkt.Entry(login_frame,font=self.entry_font)
        #Entry widget is used to accept single line text strings from a user
        self.enter_username.pack(pady=(0,15))
        #padx is taken as (0,0) by default
        #can't add pady in entry widget so add it via pack

        #For password
        tkt.Label(login_frame,text="Password",bg="#fffff0",font=self.label_font).pack()
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
        tkt.Label(registration_frame,text="Enter Your Name",bg="#fffff0",font=self.label_font).pack()
        self.register_username=tkt.Entry(registration_frame,font=self.entry_font)
        self.register_username.pack(pady=(0,15))

        #For password
        tkt.Label(registration_frame,text="Enter Password",bg="#fffff0",font=self.label_font).pack()
        self.register_password=tkt.Entry(registration_frame,show='*',font=self.entry_font)
        self.register_password.pack(pady=(0,15))
        #use self. to make them accessible across other classes

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

        tkt.Label(main_customer_frame,text=f'Greetings! {self.customer.username}',bg="#fffff0",font=self.title_font).pack()
        tkt.Label(main_customer_frame,text="Today's Menu",bg="#fffff0",font=self.label_font).pack()
        tkt.Label(main_customer_frame,text=self.menu.display(),bg="#f2f2f2",font=self.label_font).pack()

        #item to be ordered
        tkt.Label(main_customer_frame,text="What item would you wish to order?(Enter as written in Menu)",bg="#fffff0",font=self.label_font).pack()
        self.cart_item=tkt.Entry(main_customer_frame,font=self.entry_font)
        self.cart_item.pack(pady=(0,15))

        #quantity to be ordered
        tkt.Label(main_customer_frame,text="How much quantity would you like to order?",bg="#fffff0",font=self.label_font).pack()
        self.cart_item_quantity=tkt.Entry(main_customer_frame,font=self.entry_font)
        self.cart_item_quantity.pack(pady=(0,15))

        #Buttons
        tkt.Button(main_customer_frame,text="Add item to Cart",command=self.add_to_cart,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="View Cart",command=self.view_cart,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Remove item from Cart",command=self.remove_from_cart,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Order History",command=self.order_history,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Place Order",command=self.place_order,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(main_customer_frame,text="Logout",command=self.customer_logout,font=self.button_font,bg="grey",fg="black").pack()
    
              
    #to add an item to the cart
    def add_to_cart(self):
        item=self.cart_item.get()
        item_quantity=self.cart_item_quantity.get()
        if item.strip()=="":
            self.message("Please enter the name of item.",self.customer_window)
        elif not item in [i['Name'] for i in self.menu.items]:    #Note that self.menu.items is a list
            self.message(f'{item} is not available.',self.customer_window)
        else:
            for _ in range(int(item_quantity)):
                self.customer.add_item(self.menu,item)
            self.message(f'{item} x{item_quantity} has been added to your cart',self.customer_window)
                
    #to view the cart            
    def view_cart(self):
        self.message(self.customer.view_cart() if self.customer.view_cart() else "Your cart is empty",self.customer_window)

    # ui to remove item from the cart
    def remove_from_cart(self):
        self.clear_all()
        remove_from_cart_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        remove_from_cart_frame.pack()

        tkt.Label(remove_from_cart_frame,text="Remove an item from cart",bg="#fffff0",font=self.label_font).pack()
        tkt.Label(remove_from_cart_frame,text="Which item would you like to remove?",bg="#fffff0",font=self.label_font).pack()
        self.item_to_remove=tkt.Entry(remove_from_cart_frame,font=self.entry_font)
        self.item_to_remove.pack(pady=(0,15))
        tkt.Label(remove_from_cart_frame,text="Please enter the quantity to remove",bg="#fffff0",font=self.label_font).pack()
        self.quantity_to_remove=tkt.Entry(remove_from_cart_frame,font=self.entry_font)
        self.quantity_to_remove.pack(pady=(0,15))
        tkt.Button(remove_from_cart_frame,text="Remove item",command=self.item_removal, font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(remove_from_cart_frame,text="Back to order",command=self.customer_window,font=self.button_font,bg="grey",fg="black").pack()
        

    #removal of item from the cart logic
    def item_removal(self):
        item=self.item_to_remove.get()
        quantity=self.quantity_to_remove.get()

        if quantity.isdigit()==False or int(quantity)<=0 :
            self.message("Invalid quantity.",self.remove_from_cart)
        else:
            quantity=int(quantity) #because unicodes also return true in isdigit()
            cart=self.customer.view_cart()
            cart_item=[i for i in self.customer.cart if i['Name']==item]

            if not cart_item:
                self.message("There is no such item in your cart.",self.remove_from_cart)
            else:
                quantity_in_cart=len(cart_item)
                if quantity>quantity_in_cart:
                    self.message("You have entered a greater quantity than what you have in cart.",self.remove_from_cart)
                else:
                    for _ in range(int(quantity)):
                        self.customer.cart.remove(next(i for i in self.customer.cart if i['Name']==item))   #next function gets next item from an iterator  
                    self.message(f'Succesfully removed {item} x{quantity} from your cart',self.remove_from_cart) 
                
    #to display previous orders
    def order_history(self):
        previous_orders=self.order_management.read_customer_order(self.customer.username)
        previous_orders_display=""
        for order in previous_orders:
            order_display=self.order_management.order_display(order['Items Ordered'])
            total_cost=float(order['Total Cost'])
            previous_orders_display += f'{order_display} / Total Cost = ₹{total_cost:.2f}\n'
            
        self.message(previous_orders_display if previous_orders_display!="" else "Please order something which will show up here",self.customer_window)
        
    #to place and confirm the order
    def place_order(self):
        total_amount=self.customer.total_amount()
        if total_amount==0:
            self.message("Please add something to cart.",self.customer_window)
        else:
            self.clear_all()
            place_order_frame=tkt.Frame(self.root,bg="#fffff0",padx=25,pady=25)
            place_order_frame.pack()
            tkt.Label(place_order_frame,text=f'The total billing amount is ₹{total_amount:.2f}. Would you like to confirm the payment?',bg="#fffff0",font=self.label_font).pack()
            tkt.Button(place_order_frame,text="Yes",command=self.order_placement,font=self.button_font,bg="grey",fg="black").pack()
            tkt.Button(place_order_frame,text="No",command=self.customer_window,font=self.button_font,bg="grey",fg="black").pack()
            
    #the logic to place order   
    def order_placement(self):
        total_amount=self.customer.total_amount()
        self.order_management.new_order(self.customer.username,self.customer.cart)
        self.customer.process_payment()
        self.message("Your order has been placed.",self.customer_window)


    #for customer logout
    def customer_logout(self):
        self.clear_all()
        logout_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        logout_frame.pack()
        tkt.Label(logout_frame,text="Are you sure you want to logout?",bg="#fffff0",font=self.label_font).pack()
        tkt.Button(logout_frame,text="Yes",command=self.login,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(logout_frame,text="No",command=self.customer_window,font=self.button_font,bg="grey",fg="black").pack()
            
    #ui for admin
    def admin_window(self):
        self.clear_all()
        main_admin_frame=tkt.Frame(self.root,bg="#fff700",padx=25,pady=25)
        main_admin_frame.pack()
        tkt.Label(main_admin_frame,text="Greetings to The Admin",bg="#f9affa",font=self.title_font).pack()
        tkt.Button(main_admin_frame,text="Edit Menu",command=self.edit_menu,bg="grey",fg="black").pack()
        tkt.Button(main_admin_frame,text="View Menu",command=self.view_menu_admin,bg="grey",fg="black").pack()
        tkt.Button(main_admin_frame,text="View Customer Orders",command=self.select_customer,bg="grey",fg="black").pack()
        tkt.Button(main_admin_frame,text="Logout",command=self.admin_logout,bg="grey",fg="black").pack()

    #for edit menu admin
    def edit_menu(self):
        self.clear_all()
        edit_menu_frame=tkt.Frame(self.root,bg="#fff700",padx=25,pady=25)
        edit_menu_frame.pack()
        tkt.Label(edit_menu_frame,text="Menu Editor",bg="#f9affa",font=self.title_font).pack()

        #for adding item
        tkt.Label(edit_menu_frame,text="Add New item:",bg="#f9affa",font=self.label_font).pack()
        tkt.Label(edit_menu_frame,text="Which item would you like to add?",bg="#f9affa",font=self.label_font).pack()
        self.new_item=tkt.Entry(edit_menu_frame,font=self.entry_font)
        self.new_item.pack(pady=(0,15))
        tkt.Label(edit_menu_frame,text="What will be the item price?",bg="#f9affa",font=self.label_font).pack()
        self.new_item_price=tkt.Entry(edit_menu_frame,font=self.entry_font)
        self.new_item_price.pack(pady=(0,15))
        tkt.Button(edit_menu_frame,command=self.item_add_admin,text="Add",bg="grey",fg="black").pack()

        #for removing item
        tkt.Label(edit_menu_frame,text="Remove an item:",bg="#f9affa",font=self.label_font).pack()
        tkt.Label(edit_menu_frame,text="Which item would you like to remove?",bg="#f9affa",font=self.label_font).pack()
        self.remove_item=tkt.Entry(edit_menu_frame,font=self.entry_font)
        self.remove_item.pack(pady=(0,15))
        tkt.Button(edit_menu_frame,command=self.item_removal_admin,text="Remove",bg="grey",fg="black").pack()

        #for back navigation
        tkt.Button(edit_menu_frame,command=self.admin_window,text="Back to home screen",bg="grey",fg="black").pack()
    
    #for item add logic admin
    def item_add_admin(self):
        new_item=self.new_item.get()
        new_item_price=self.new_item_price.get()

        if new_item.strip()=="":
            self.message("Enter a valid item name.",self.edit_menu)
        else:
            if new_item_price.strip()=="" or new_item_price.isdigit()==False:
                self.message("Enter a valid item price.",self.edit_menu)
            else:
                new_item_price=float(new_item_price)
                if new_item in [i['Name'] for i in self.menu.items]:
                    self.message("This item is already in the Menu.",self.edit_menu)
                else:
                    self.menu.add_new_item(new_item,new_item_price)
                    self.message("Item has been succesfully added.",self.edit_menu)

    #for item remove logic admin
    def item_removal_admin(self):
        item_to_remove=self.remove_item.get()
        
        if item_to_remove.strip()=="":
            self.message("Enter a valid item name.",self.edit_menu)
        else:
            if item_to_remove not in [i['Name'] for i in self.menu.items]:
                self.message("This item does not exist in the Menu.",self.edit_menu)
            else:
                self.menu.remove_old_item(item_to_remove)
                self.message("Succesfully removed the item from Menu.",self.edit_menu)

    #to view the current menu
    def view_menu_admin(self):
        if self.menu.display():
            self.message(self.menu.display(),self.admin_window)
        else:
            self.message("Please add items, the menu is empty.",self.admin_window)

    #to view the customer's order's
    def select_customer(self):
        self.clear_all()
        select_customer_frame= tkt.Frame(self.root,bg="#fff700",padx=25,pady=25)
        select_customer_frame.pack()
        tkt.Label(select_customer_frame,text="Select whose Orders you want to see",bg="#f9affa",font=self.label_font).pack()

        #making the box which contains the list of customers to select from using listbox widget
        self.customer_selector=tkt.Listbox(select_customer_frame,font=self.label_font)
        self.customer_selector.pack()
        customer_listing=self.customer_management.read_customers()
        for i in customer_listing:
            self.customer_selector.insert(tkt.END,i['username']) #tkt.END = inserts the elements at end of list

        #Buttons
        tkt.Button(select_customer_frame,text="Open Order History",command=self.view_order_of_selection,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(select_customer_frame,text="Back to home screen",command=self.admin_window,font=self.button_font,bg="grey",fg="black").pack()

    #to display the selected customer's order history
    def view_order_of_selection(self):
        selection=self.customer_selector.curselection() #returns a tuple of index of the selection
        if selection==():
            self.message("Select one customer.",self.select_customer)
        else:
            #same logic as order history for customer
            customer_selection=self.customer_selector.get(selection)        
            previous_orders=self.order_management.read_customer_order(customer_selection)
            previous_orders_display=""
            for order in previous_orders:
                order_display=self.order_management.order_display(order['Items Ordered'])
                total_cost=float(order['Total Cost'])
                previous_orders_display += f'{order_display} / Total Cost = ₹{total_cost:.2f}\n'
            
            self.message(previous_orders_display if previous_orders_display!="" else "No oders to show",self.select_customer)
  

    #to logout for the admin
    def admin_logout(self):
        self.clear_all()
        logout_frame=tkt.Frame(self.root,bg="#fff700",padx=25,pady=25)
        logout_frame.pack()
        tkt.Label(logout_frame,text="Are you sure you want to logout?",bg="#f9affa",font=self.label_font).pack()
        tkt.Button(logout_frame,text="Yes",command=self.login,font=self.button_font,bg="grey",fg="black").pack()
        tkt.Button(logout_frame,text="No",command=self.admin_window,font=self.button_font,bg="grey",fg="black").pack()
        
        
        
        
     
    
        
        
            
    
        

        
        
        
            
        
