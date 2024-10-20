import tkinter as tkt
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import font
from file_manager import OrderManager, CustomerManager, MenuManager
import csv


class UI:
    def __init__(self, menu, customer, admin):
        self.menu = menu
        self.customer = customer
        self.admin = admin
        self.order_management = OrderManager()
        self.customer_management = CustomerManager()
        self.root = tkt.Tk()  # Creates the main window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("CuisineControl")  # Creates the title
        # self.root.attributes("-fullscreen", True)
        self.theme()

        # self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))

        """This method has been created so that we don't need to adjust
           format multiple times"""
        self.run()
        """This method has been created so that the application keeps
           running"""

    # The below method is the format which will be followed through the code
    def theme(self):
        self.root.configure(bg="#e6f7ff")

        self.title_font = font.Font(family="Georgia", size=20, weight="bold")
        self.label_font = font.Font(family="Garamond", size=18)
        self.entry_font = font.Font(family="Manhattan", size=18)
        self.button_font = font.Font(family="Consolas", size=16)

    # The below method will clear all the existing UI to prepare for new UI
    def add_header(self):
        header = tkt.Label(self.root, text="CuisineControl", bg="navyblue", fg="lightblue",
                           font=("Helvetica", 25, "bold"), pady=20)
        header.pack(side="top", fill="x")

    def add_footer(self):
        footer = tkt.Label(self.root, text="Footer Text", bg="navyblue", fg="lightblue",
                           font=("Helvetica", 20, "bold"), pady=20)
        footer.pack(side="bottom", fill="x")

    def draw_rounded_rectangle(self, canvas, color):
        x0, y0, x1, y1 = 0, 0, 400, 50  # Coordinates for the rectangle
        radius = 20  # Radius for the rounded corners
        canvas.create_arc(x0, y0, x0 + radius, y0 + radius, start=90, extent=90, fill=color, outline=color)
        canvas.create_arc(x1 - radius, y0, x1, y0 + radius, start=0, extent=90, fill=color, outline=color)
        canvas.create_arc(x0, y1 - radius, x0 + radius, y1, start=180, extent=90, fill=color, outline=color)
        canvas.create_arc(x1 - radius, y1 - radius, x1, y1, start=270, extent=90, fill=color, outline=color)
        canvas.create_rectangle(x0 + radius / 2, y0, x1 - radius / 2, y1, fill=color, outline=color)
        canvas.create_rectangle(x0, y0 + radius / 2, x1, y1 - radius / 2, fill=color, outline=color)

    def clear_all(self):
        for i in self.root.winfo_children():
            i.destroy()

    # used to ensure that the program keeps running
    def run(self):
        self.login()
        self.root.mainloop()  # used to ensure that the window stays open

    # The below method is used to ensure no pop-ups are there, and UI remains in the same window
    def message(self, message, go_back_to):
        self.clear_all()
        # message_frame = tkt.Frame(self.root, bg="#e6f7ff", padx=25, pady=25)
        # message_frame.pack()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        message_frame = ttk.Label(self.root, image=converted_image)
        message_frame.pack(fill='both', expand=True)
        message_frame.image = converted_image

        tkt.Label(message_frame, text=message, bg="#fffff0", font=self.label_font).pack(anchor="center")
        tkt.Button(message_frame, text="Got it!", command=go_back_to, font=self.button_font, bg="#232323",
                   fg="white").pack(anchor="center")

    # The below method is used to login
    def login(self):
        self.clear_all()
        # self.add_header()
        # frames are used to hold other widgets
        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        label = ttk.Label(self.root, image=converted_image)
        label.pack(fill='both', expand=True)
        label.image = converted_image

        # login_frame = tkt.Frame(self.root,bg="black", padx=25, pady=100)
        # login_frame.pack(fill='both', expand=True)
        # padx is for horizontal padding, pady is for vertical padding
        # login_frame.pack()

        # this .pack() method calls the login_frame to the window

        # self.check = tkt.Checkbutton(self.root,text="Show Password",font=("Bold",10),bg="#232323",fg="grey").place(x=960,y=465,anchor= "center")

        # For username
        tkt.Label(self.root, text="Username :", bg="#232323", fg="white", font=self.label_font).place(x=750, y=350,
                                                                                                      anchor="center")
        # pack method was not used before in just a single line because it will return None but here it is not an issue
        self.enter_username = tkt.Entry(self.root, font=self.entry_font)
        # Entry widget is used to accept single line text strings from a user
        self.enter_username.place(x=1000, y=350, anchor="center")
        # padx is taken as (0,0) by default
        # can't add pady in entry widget so add it via pack

        # For password
        tkt.Label(self.root, text="Password  :", bg="#232323", fg="white", font=self.label_font).place(x=749, y=420,
                                                                                                       anchor="center")
        # self.enter_password = tkt.Entry(self.root, show="*", font=self.entry_font) # by default
        # self.enter_password.place(x=1000,y=420,anchor= "center")

        # self.check = tkt.Checkbutton(self.root,text="Show Password",font=("Bold",10),bg="#232323",fg="grey",variable=tkt.BooleanVar(),command=self.toggle_password).place(x=960,y=465,anchor= "center")

        self.enter_password = tkt.Entry(self.root, show="*", font=self.entry_font)

        self.enter_password.place(x=1000, y=420, anchor="center")

        self.check = tkt.Checkbutton(self.root, text="Show Password", font=("Bold", 10), bg="#232323", fg="grey",
                                     command=self.toggle_password).place(x=960, y=465, anchor="center")

        # For buttons
        tkt.Button(self.root, text="Login as Customer", bg="black", fg="white", command=self.login_customer,
                   font=self.button_font).place(relx=0.5, y=515, anchor="center")
        tkt.Button(self.root, text="Login as Admin", command=self.login_admin, font=self.button_font, bg="black",
                   fg="white").place(relx=0.5, y=565, anchor="center")
        tkt.Button(self.root, text="Registration for New Customers", command=self.register_customer,
                   font=self.button_font, bg="black", fg="white").place(relx=0.5, y=615, anchor="center")
        self.add_footer()

    def toggle_password(self):
        if self.enter_password.cget("show") == "*":
            self.enter_password.config(show="")  # Show password
        else:
            self.enter_password.config(show="*")  # Hide password

    # used to validate the customer login
    def login_customer(self):
        username = self.enter_username.get()
        password = self.enter_password.get()
        if self.customer.login(username, password) is True:
            self.customer_window()
        else:
            self.message("Invalid Username or Password.", self.login)

    # used to validate the admin login
    def login_admin(self):
        username = self.enter_username.get()
        password = self.enter_password.get()
        if self.admin.validate(username, password) is True:
            self.admin_window()
        else:
            self.message("Invalid username or Password.", self.login)

    # The below UI will be for new customer registration
    # def register_customer(self):
    #     self.clear_all()
    #     self.add_header()
    #     registration_frame = tkt.Frame(self.root, bg="#e6f7ff", padx=25, pady=25)
    #     registration_frame.pack(fill='both', expand=True)

    #     # For username
    #     tkt.Label(registration_frame, text="Enter Your Name", bg="#fffff0", font=self.label_font).pack()
    #     self.register_username = tkt.Entry(registration_frame, font=self.entry_font)
    #     self.register_username.pack(pady=(0, 15))

    #     # For password
    #     tkt.Label(registration_frame, text="Enter Password", bg="#fffff0", font=self.label_font).pack()
    #     self.register_password = tkt.Entry(registration_frame, show='*', font=self.entry_font)
    #     self.register_password.pack(pady=(0, 15))
    #     # use self. to make them accessible across other classes

    #     # For buttons
    #     tkt.Button(registration_frame, text="Register Yourself", command=self.new_customer, font=self.button_font,
    #                bg="grey", fg="black").pack()
    #     tkt.Button(registration_frame, text="Back to Login Page", command=self.login, font=self.button_font, bg="grey",
    #                fg="black").pack()
    def register_customer(self):
        self.clear_all()
        self.add_header()
        photo3 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo3)
        message_frame = ttk.Label(self.root, image=converted_image)
        message_frame.pack(fill='both', expand=True)
        message_frame.image = converted_image

        # For username
        tkt.Label(message_frame, text="Enter Your Name", bg="#232323",fg="white", font=self.label_font).place(x=730, y=350,
                                                                                                      anchor="center")
        self.register_username = tkt.Entry(message_frame, font=self.entry_font)
        self.register_username.place(x=1000, y=350, anchor="center")


        # For password
        tkt.Label(message_frame, text="Enter Password", bg="#232323",fg="white", font=self.label_font).place(x=725, y=420,
                                                                                                       anchor="center")
        self.register_password = tkt.Entry(message_frame, show='*', font=self.entry_font)
        self.register_password.place(x=1000, y=420, anchor="center")
        # use self. to make them accessible across other classes

        # For buttons
        tkt.Button(message_frame, text="Register Yourself", command=self.new_customer, font=self.button_font,
                   bg="black", fg="white").place(relx=0.5, y=505, anchor="center")
        tkt.Button(message_frame, text="Back to Login Page", command=self.login, font=self.button_font, bg="black",
                   fg="white").place(relx=0.5, y=555, anchor="center")

    # registration logic for new customers
    def new_customer(self):
        username = self.register_username.get()
        password = self.register_password.get()

        # checks for no username/password
        if not username.strip() or not password.strip():
            self.message("Please fill username and password.", self.register_customer)
            return  # needs to stop execution
        # checks for same username as other
        if self.customer_management.invalid_username(username):
            self.message("Username not available. Please enter another one.", self.register_customer)
            return

        # valid registration
        self.customer.registration(username, password)
        self.message("You have been Registered. Please login to proceed", self.login)

    # The main page for customer UI
    def customer_window(self):
        self.clear_all()
        self.add_header()
        #
        # # Create the main frame for the customer window
        # main_customer_frame = tkt.Frame(self.root, bg="#e6f7ff", padx=25, pady=25)
        # main_customer_frame.pack(fill='both', expand=True)
        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        main_customer_frame = ttk.Label(self.root, image=converted_image)
        main_customer_frame.pack(fill='both', expand=True)
        main_customer_frame.image = converted_image

        greeting_label = tkt.Label(main_customer_frame, text=f'Greetings! {self.customer.username}', bg="darkgrey",
                                   fg="#232323", font=("Helvetica", 30, "bold"))
        greeting_label.pack(side="top", anchor="nw")

        # Create a frame for the table and images
        menu_frame = tkt.Frame(main_customer_frame, bg="#232323")
        # menu_frame.pack(fill='both', expand=True)
        menu_frame.pack()

        # Use grid in menu_frame to hold the table layout
        menu_frame.grid_columnconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(1, weight=1)
        menu_frame.grid_columnconfigure(2, weight=1)
        menu_frame.grid_columnconfigure(3, weight=1)

        # Add the menu table headings (manually create as Treeview doesn’t support widgets)
        headings = ['Item Name', 'Image', 'Price (₹)', 'Quantity', 'Actions']
        for idx, heading in enumerate(headings):
            tkt.Label(menu_frame, text=heading, bg="lightgrey", fg="black", font=self.label_font).grid(row=0,
                                                                                                       column=idx,
                                                                                                       padx=10, pady=5)

        # Load the menu from the CSV file
        self.load_menu_from_csv(menu_frame)

        # Add buttons for cart management and order placement
        tkt.Button(main_customer_frame, text="View Cart", command=self.view_cart, font=self.button_font, bg="#232323",
                   fg="white").pack(pady=20)
        tkt.Button(main_customer_frame, text="Order History", command=self.order_history, font=self.button_font,
                   bg="#232323", fg="white").pack()
        tkt.Button(main_customer_frame, text="Place Order-->", command=self.place_order, font=("Helvetica", 30),
                   bg="lightblue", fg="navyblue").place(relx=1.0, rely=1.0, anchor='se')
        tkt.Button(main_customer_frame, text="Logout", command=self.customer_logout, font=("Helvetica", 30), bg="red",
                   fg="white").place(relx=0, rely=1.0, anchor='sw')
        self.add_footer()

    def load_menu_from_csv(self, parent_frame):
        """Load menu items from the CSV file"""
        try:
            with open('menu.csv', mode='r') as file:
                reader = csv.DictReader(file)
                row_index = 1  # Start from row 1 as row 0 is used for the table headers
                for row in reader:
                    # Each row contains 'Name', 'Price', and 'ImagePath' columns
                    item = {
                        'Name': row['Name'],
                        'Price': float(row['Price']),
                        'ImagePath': row['ImagePath']
                    }
                    self.add_menu_item(item, parent_frame, row_index)
                    row_index += 1
        except FileNotFoundError:
            print("The menu.csv file was not found.")


    def add_menu_item(self, item, parent_frame, row_index):
        """Helper method to add menu items (name, image, price, quantity) in grid format"""
        item_name = item['Name']
        item_price = item['Price']
        item_image_path = item.get('ImagePath', 'default_food.jpg')  # Use default if image path is missing

        # Load the image for each item
        try:
            image = Image.open(item_image_path)
        except FileNotFoundError:
            image = Image.open('default_food.jpg')  # Load default image if not found

        image = image.resize((50, 50))  # Resize the image
        image_tk = ImageTk.PhotoImage(image)

        # Store the image in a list or as an instance variable to avoid garbage collection
        if not hasattr(self, 'images'):
            self.images = []  # Create a list to store image references

        self.images.append(image_tk)  # Append the image reference to prevent garbage collection

        # Create a Label to display the image
        image_label = tkt.Label(parent_frame, image=image_tk, bg="white")
        image_label.grid(row=row_index, column=1, padx=10, pady=5)

        # Create buttons for incrementing and decrementing quantity
        quantity_var = tkt.IntVar(value=0)  # Initial quantity is 0

        # Fix for unresolved reference: Make sure item is passed correctly in lambda
        inc_button = tkt.Button(
            parent_frame,
            text='+',
            command=lambda i=item, q_var=quantity_var: self.update_quantity(i, q_var, delta=1, sigma=0)
        )

        dec_button = tkt.Button(
            parent_frame,
            text='-',
            command=lambda i=item, q_var=quantity_var: self.update_quantity(i, q_var, delta=0, sigma=1)
        )

        quantity_label = tkt.Label(parent_frame, textvariable=quantity_var, bg="#232323", fg="white",
                                   font=self.label_font)

        # Place the elements in the grid
        tkt.Label(parent_frame, text=item_name, bg="#232323", fg="white", font=self.label_font).grid(row=row_index,
                                                                                                     column=0,
                                                                                                     padx=10,
                                                                                                     pady=5)  # Item name
        tkt.Label(parent_frame, text=f"₹{item_price:.2f}", bg="#232323", fg="white", font=self.label_font).grid(
            row=row_index,
            column=2, padx=10,
            pady=5)  # Price
        quantity_label.grid(row=row_index, column=3, padx=10, pady=5)  # Quantity
        dec_button.grid(row=row_index, column=4, padx=5, pady=5, sticky='e')  # Decrease button
        inc_button.grid(row=row_index, column=4, padx=5, pady=5, sticky='w')  # Increase button

    def update_quantity(self, item, quantity_var, delta, sigma):
        """Update the quantity of the item when the + or - button is pressed"""
        current_quantity = quantity_var.get()
        new_quantity = current_quantity + delta - sigma

        if new_quantity >= 0:  # Prevent negative quantities
            quantity_var.set(new_quantity)

            # Update the cart accordingly
            if delta > 0:  # Increment logic (+ button)
                self.customer.add_item(self.menu, item['Name'])

            elif sigma > 0:  # Decrement logic (- button)
                if new_quantity == 0:  # If the quantity reaches zero, remove the item from the cart
                    self.customer.remove_item(self.menu, item['Name'])  # Assuming remove_item is implemented

                else:  # If the quantity is still above zero, reduce the quantity
                    self.customer.sub_item(self.menu, item['Name'])


    # to add an item to the cart

    def add_to_cart(self):
        item = self.cart_item.get()
        item_quantity = self.cart_item_quantity.get()
        if item.strip() == "":
            self.message("Please enter the name of item.", self.customer_window)
        elif not item in [i['Name'] for i in self.menu.items]:  # Note that self.menu.items is a list
            self.message(f'{item} is not available.', self.customer_window)
        else:
            for _ in range(int(item_quantity)):
                self.customer.add_item(self.menu, item)
            self.message(f'{item} x{item_quantity} has been added to your cart', self.customer_window)

    # to view the cart
    def view_cart(self):
        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        main_customer_frame = ttk.Label(self.root, image=converted_image)
        main_customer_frame.pack(fill='both', expand=True)
        main_customer_frame.image = converted_image

        self.message(self.customer.view_cart() if self.customer.view_cart() else "Your cart is empty",
                     self.customer_window)

    # ui to remove item from the cart
    def remove_from_cart(self):
        self.clear_all()
        remove_from_cart_frame = tkt.Frame(self.root, bg="#e6f7ff", padx=25, pady=25)
        remove_from_cart_frame.pack()

        tkt.Label(remove_from_cart_frame, text="Remove an item from cart", bg="#fffff0", font=self.label_font).pack()
        tkt.Label(remove_from_cart_frame, text="Which item would you like to remove?", bg="#fffff0",
                  font=self.label_font).pack()
        self.item_to_remove = tkt.Entry(remove_from_cart_frame, font=self.entry_font)
        self.item_to_remove.pack(pady=(0, 15))
        tkt.Label(remove_from_cart_frame, text="Please enter the quantity to remove", bg="#fffff0",
                  font=self.label_font).pack()
        self.quantity_to_remove = tkt.Entry(remove_from_cart_frame, font=self.entry_font)
        self.quantity_to_remove.pack(pady=(0, 15))
        tkt.Button(remove_from_cart_frame, text="Remove item", command=self.item_removal, font=self.button_font,
                   bg="grey", fg="black").pack()
        tkt.Button(remove_from_cart_frame, text="Back to order", command=self.customer_window, font=self.button_font,
                   bg="grey", fg="black").pack()

    # removal of item from the cart logic
    def item_removal(self):
        item = self.item_to_remove.get()
        quantity = self.quantity_to_remove.get()

        if quantity.isdigit() == False or int(quantity) <= 0:
            self.message("Invalid quantity.", self.remove_from_cart)
        else:
            quantity = int(quantity)  # because unicodes also return true in isdigit()
            cart = self.customer.view_cart()
            cart_item = [i for i in self.customer.cart if i['Name'] == item]

            if not cart_item:
                self.message("There is no such item in your cart.", self.remove_from_cart)
            else:
                quantity_in_cart = len(cart_item)
                if quantity > quantity_in_cart:
                    self.message("You have entered a greater quantity than what you have in cart.",
                                 self.remove_from_cart)
                else:
                    for _ in range(int(quantity)):
                        self.customer.cart.remove(next(i for i in self.customer.cart if i[
                            'Name'] == item))  # next function gets next item from an iterator
                    self.message(f'Succesfully removed {item} x{quantity} from your cart', self.remove_from_cart)

                    # to display previous orders

    def order_history(self):
        self.clear_all()
        self.add_header()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        order_history_frame = ttk.Label(self.root, image=converted_image)
        order_history_frame.pack(fill='both', expand=True)
        order_history_frame.image = converted_image


        # Create a Treeview widget (table)
        columns = ('order_number', 'items', 'total_cost')
        tree = ttk.Treeview(order_history_frame, columns=columns, show='headings', height=10)

        # Define column headings
        tree.heading('order_number', text='Order Number', anchor='center')
        tree.heading('items', text='Items Ordered', anchor='center')
        tree.heading('total_cost', text='Total Cost (₹)', anchor='center')

        # Define column widths
        tree.column('order_number', width=150, anchor='center')
        tree.column('items', width=300, anchor='center')
        tree.column('total_cost', width=150, anchor='center')

        # Style the Treeview
        tree_style = ttk.Style()
        tree_style.configure("Treeview", rowheight=40, borderwidth=1, relief='solid', font=('Helvetica', 14))
        tree_style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        # Pack the treeview (table)
        tree.pack()

        # Alternating row colors (simulating row lines)
        tree.tag_configure('oddrow', background='#f2f2f2')  # Light grey for odd rows
        tree.tag_configure('evenrow', background='#ffffff')  # White for even rows

        # Fetch order history data
        previous_orders = self.order_management.read_customer_order(self.customer.username)

        # Insert data into the table
        for index, order in enumerate(previous_orders, start=1):
            items_ordered = self.order_management.order_display(order['Items Ordered'])
            total_cost = float(order['Total Cost'])
            if index % 2 == 0:
                tree.insert('', 'end', values=(index, items_ordered, f'₹{total_cost:.2f}'), tags=('evenrow',))
            else:
                tree.insert('', 'end', values=(index, items_ordered, f'₹{total_cost:.2f}'), tags=('oddrow',))

        # Add a back button
        tkt.Button(order_history_frame, text="Back", command=self.customer_window, font=self.button_font, bg="#232323",
                   fg="white").pack(pady=20)

    # to place and confirm the order
    def place_order(self):
        total_amount = self.customer.total_amount()
        if total_amount == 0:
            self.message("Please add something to cart.", self.customer_window)
        else:
            self.clear_all()
            # place_order_frame = tkt.Frame(self.root, bg="#fffff0", padx=25, pady=25)
            # place_order_frame.pack()

            photo2 = Image.open("bg1.png")
            converted_image = ImageTk.PhotoImage(photo2)
            place_order_frame = ttk.Label(self.root, image=converted_image)
            place_order_frame.pack(fill='both', expand=True)
            place_order_frame.image = converted_image

            tkt.Label(place_order_frame,
                      text=f'The total billing amount is ₹{total_amount:.2f}. Would you like to confirm the payment?',
                      bg="#fffff0", font=self.label_font).pack()
            tkt.Button(place_order_frame, text="Yes", command=self.order_placement, font=self.button_font, bg="#232323",
                       fg="white").pack()
            tkt.Button(place_order_frame, text="No", command=self.customer_window, font=self.button_font, bg="#232323",
                       fg="white").pack()

    # the logic to place order
    def order_placement(self):
        total_amount = self.customer.total_amount()
        self.order_management.new_order(self.customer.username, self.customer.cart)
        self.customer.process_payment()
        self.message("Your order has been placed.", self.customer_window)

    # for customer logout
    def customer_logout(self):
        self.clear_all()
        self.add_header()
        logout_frame = tkt.Frame(self.root, bg="#e6f7ff", padx=25, pady=25)
        logout_frame.pack()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        logout_frame = ttk.Label(self.root, image=converted_image)
        logout_frame.pack(fill='both', expand=True)
        logout_frame.image = converted_image

        tkt.Label(logout_frame, text="Are you sure you want to logout?", bg="#fffff0", font=self.label_font).pack()
        tkt.Button(logout_frame, text="Yes", command=self.login, font=self.button_font, bg="#232323", fg="white").pack()
        tkt.Button(logout_frame, text="No", command=self.customer_window, font=self.button_font, bg="#232323",
                   fg="white").pack()

    # ui for admin
    # def admin_window(self):
    #     self.clear_all()
    #     self.add_header()
    #     main_admin_frame = tkt.Frame(self.root, bg="#fff700", padx=25, pady=25)
    #     main_admin_frame.pack()

    #     photo2 = Image.open("bg1.png")
    #     converted_image = ImageTk.PhotoImage(photo2)
    #     main_admin_frame = ttk.Label(self.root, image=converted_image)
    #     main_admin_frame.pack(fill='both', expand=True)
    #     main_admin_frame.image = converted_image

    #     tkt.Label(main_admin_frame, text="Greetings to The Admin", bg="#fffff0", font=self.title_font).pack()
    #     tkt.Button(main_admin_frame, text="Edit Menu", command=self.edit_menu,font = ('Helvetica',30), bg="grey", fg="black").pack()
    #     tkt.Button(main_admin_frame, text="View Menu", command=self.view_menu_admin,font = ('Helvetica',30), bg="grey", fg="black").pack()
    #     tkt.Button(main_admin_frame, text="View Customer Orders", command=self.select_customer,font = ('Helvetica',30), bg="grey",
    #                fg="black").pack()
    #     tkt.Button(main_admin_frame, text="Logout", command=self.admin_logout,font = ('Helvetica',30),bg="red", fg="black").place(relx = 0.05,rely = 0.9,anchor = 'center')


    def admin_window(self):
        self.clear_all()
        self.add_header()
        main_admin_frame = tkt.Frame(self.root, bg="#fff700", padx=25, pady=25)
        main_admin_frame.pack()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        main_admin_frame = ttk.Label(self.root, image=converted_image)
        main_admin_frame.pack(fill='both', expand=True)
        main_admin_frame.image = converted_image

        tkt.Label(main_admin_frame, text="Greetings to The Admin", bg="#232323",fg="white", font=('Helvetica',30,"bold")).pack(anchor="center")
        tkt.Button(main_admin_frame, text="Edit Menu", command=self.edit_menu,font = ('Helvetica',25), bg="black", fg="white").place(relx=0.5,rely=0.3,anchor="center")
        tkt.Button(main_admin_frame, text="View Menu", command=self.view_menu_admin,font = ('Helvetica',25), bg="black", fg="white").place(relx=0.5,rely=0.4,anchor="center")
        tkt.Button(main_admin_frame, text="View Customer Orders", command=self.select_customer,font = ('Helvetica',25), bg="black",
                   fg="white").place(relx=0.5,rely=0.5,anchor="center")
        tkt.Button(main_admin_frame, text="Logout", command=self.admin_logout,font = ('Helvetica',30),bg="red", fg="black").place(relx = 0.05,rely = 0.9,anchor = 'center')

    # for edit menu admin
    def edit_menu(self):
        self.clear_all()
        self.add_header()
        edit_menu_frame = tkt.Frame(self.root, bg="#fff700", padx=25, pady=25)
        edit_menu_frame.pack()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        edit_menu_frame = ttk.Label(self.root, image=converted_image)
        edit_menu_frame.pack(fill='both', expand=True)
        edit_menu_frame.image = converted_image

        tkt.Label(edit_menu_frame, text="Menu Editor", bg="#fffff0", font=self.title_font).pack()

        # for adding item
        tkt.Label(edit_menu_frame, text="Add New item:", bg="#fffff0", font=self.label_font).pack()
        tkt.Label(edit_menu_frame, text="Which item would you like to add?", bg="#fffff0", font=self.label_font).pack()
        self.new_item = tkt.Entry(edit_menu_frame, font=self.entry_font)
        self.new_item.pack(pady=(0, 15))
        tkt.Label(edit_menu_frame, text="What will be the item price?", bg="#fffff0", font=self.label_font).pack()
        self.new_item_price = tkt.Entry(edit_menu_frame, font=self.entry_font)
        self.new_item_price.pack(pady=(0, 15))
        tkt.Label(edit_menu_frame, text="Mention the Image path.", bg="#fffff0", font=self.label_font).pack()
        self.new_item_ImagePath = tkt.Entry(edit_menu_frame, font=self.entry_font)
        self.new_item_ImagePath.pack(pady=(0, 15))
        tkt.Button(edit_menu_frame, command=self.item_add_admin, text="Add", bg="grey", fg="black").pack()

        # for removing item
        tkt.Label(edit_menu_frame, text="Remove an item:", bg="#fffff0", font=self.label_font).pack()
        tkt.Label(edit_menu_frame, text="Which item would you like to remove?", bg="#fffff0",
                  font=self.label_font).pack()
        self.remove_item = tkt.Entry(edit_menu_frame, font=self.entry_font)
        self.remove_item.pack(pady=(0, 15))
        tkt.Button(edit_menu_frame, command=self.item_removal_admin, text="Remove", bg="grey", fg="black").pack()

        # for back navigation
        tkt.Button(edit_menu_frame, command=self.admin_window, text="Back to home screen", bg="grey", fg="black").pack()

    # for item add logic admin
    def item_add_admin(self):
        new_item = self.new_item.get()
        new_item_price = self.new_item_price.get()
        new_item_ImagePath = self.new_item_ImagePath.get()

        if new_item.strip() == "":
            self.message("Enter a valid item name.", self.edit_menu)
        else:
            if new_item_price.strip() == "" or new_item_price.isdigit() == False:
                self.message("Enter a valid item price.", self.edit_menu)
            else:
                new_item_price = float(new_item_price)
                if new_item in [i['Name'] for i in self.menu.items]:
                    self.message("This item is already in the Menu.", self.edit_menu)
                else:
                    self.menu.add_new_item(new_item, new_item_price,new_item_ImagePath)
                    self.message("Item has been succesfully added.", self.edit_menu)

    # for item remove logic admin
    def item_removal_admin(self):
        item_to_remove = self.remove_item.get()

        if item_to_remove.strip() == "":
            self.message("Enter a valid item name.", self.edit_menu)
        else:
            if item_to_remove not in [i['Name'] for i in self.menu.items]:
                self.message("This item does not exist in the Menu.", self.edit_menu)
            else:
                self.menu.remove_old_item(item_to_remove)
                self.message("Succesfully removed the item from Menu.", self.edit_menu)

    # to view the current menu
    def view_menu_admin(self):
        if self.menu.display():
            self.message(self.menu.display(), self.admin_window)
        else:
            self.message("Please add items, the menu is empty.", self.admin_window)

    # to view the customer's order's
    def select_customer(self):
        self.clear_all()
        self.add_header()
        select_customer_frame = tkt.Frame(self.root, bg="#fff700", padx=25, pady=25)
        select_customer_frame.pack()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        select_customer_frame = ttk.Label(self.root, image=converted_image)
        select_customer_frame.pack(fill='both', expand=True)
        select_customer_frame.image = converted_image

        tkt.Label(select_customer_frame, text="Select whose Orders you want to see", bg="#fffff0",
                  font=self.label_font).pack()

        # making the box which contains the list of customers to select from using listbox widget
        self.customer_selector = tkt.Listbox(select_customer_frame, font=self.label_font)
        self.customer_selector.pack()
        customer_listing = self.customer_management.read_customers()
        for i in customer_listing:
            self.customer_selector.insert(tkt.END, i['username'])  # tkt.END = inserts the elements at end of list

        # Buttons
        tkt.Button(select_customer_frame, text="Open Order History", command=self.view_order_of_selection,
                   font=self.button_font, bg="grey", fg="black").pack()
        tkt.Button(select_customer_frame, text="Back to home screen", command=self.admin_window, font=self.button_font,
                   bg="grey", fg="black").pack()

    # to display the selected customer's order history
    def view_order_of_selection(self):
        selection = self.customer_selector.curselection()  # returns a tuple of index of the selection
        if selection == ():
            self.message("Select one customer.", self.select_customer)
        else:
            # same logic as order history for customer
            customer_selection = self.customer_selector.get(selection)
            previous_orders = self.order_management.read_customer_order(customer_selection)
            previous_orders_display = ""
            for order in previous_orders:
                order_display = self.order_management.order_display(order['Items Ordered'])
                total_cost = float(order['Total Cost'])
                previous_orders_display += f'{order_display} / Total Cost = ₹{total_cost:.2f}\n'

            self.message(previous_orders_display if previous_orders_display != "" else "No oders to show",
                         self.select_customer)

    # to logout for the admin
    def admin_logout(self):
        self.clear_all()
        self.add_header()
        logout_frame = tkt.Frame(self.root, bg="#fff700", padx=25, pady=25)
        logout_frame.pack()

        photo2 = Image.open("bg1.png")
        converted_image = ImageTk.PhotoImage(photo2)
        logout_frame = ttk.Label(self.root, image=converted_image)
        logout_frame.pack(fill='both', expand=True)
        logout_frame.image = converted_image

        tkt.Label(logout_frame, text="Are you sure you want to logout?", bg="#fffff0", font=self.label_font).pack()
        tkt.Button(logout_frame, text="Yes", command=self.login, font=self.button_font, bg="grey", fg="black").pack()
        tkt.Button(logout_frame, text="No", command=self.admin_window, font=self.button_font, bg="grey",
                   fg="black").pack()
