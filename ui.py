import tkinter as tkt
from tkinter import font
from file_manager import OrderManager,CustomerManager


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
        self.label_font=font.Font(family="Garamond",size=16)
        self.button_font=font.Font(family="Consolas",size=16)

    #The below method will clear all the existing UI to prepare for new UI
    def clear_all(self):
        for i in self.root.winfo_children():
            i.destroy()


    #The below method will be used for login UI
    def login(self):
        self.clear_all()
        #frames are used to hold other widgets
        login_frame=tkt.Frame(self.root,bg="#e6f7ff",padx=25,pady=25)
        #padx is for horizontal padding, pady is for vertical padding
        login_frame.pack()
        #this .pack() method calls the login_frame to the window

        #For username
        tkt.Label(login_frame,text="Username",bg="#0d1117",font=self.label_font).pack()
        #pack method was not used before in just a single line because it will return None but here it is not an issue
        self.enter_username=tkt.Entry(login_frame,font=self.label_font)
        #Entry widget is used to accept single line text strings from a user
        self.enter_username.pack(pady=(0,15))
        #padx is taken as (0,0) by default

        #For password
        tkt.Label(login_frame,text="Password",bg="#0d1117",font=self.label_font).pack()
        self.enter_password=tkt.Entry(login_frame,show="*",font=self.label_font)
        self.enter_password.pack(pady=(0,15))

    def run(self):
        self.login()
        self.root.mainloop() #used to ensure that the window stays open

        
        

        
        
        
            
        
