import csv

#This class is to manage all the login stuff related to the customers

class CustomerManager:

    def __init__(self,file='customers.csv'):
        self.file=file

    #The below method will append a new customer to the csv file

    def customer_registration(self,username,password):

        with open(self.file,mode='a',newline='') as file:
            """This will open the file: "self.file" which holds the customer data
           and mode='a' will append the data at the end of the file without
           overwriting exisitng stuff. Newline='' will ensure that no extra lines
           are added b/w rows. It will assign this opened file to the variable
           file"""

            writer=csv.writer(file)
            """Creating a variable named writer which holds the csv
               writer object, the csv.writer function creates a
               writer object which is used to write rows into the
               file which is passed as a parameter"""

            writer.writerow([username, password])
            """This method will write a single row in the csv file
               and the single row is the list that will be written"""

    #The below method will check if the customer is using a previously used name

    def invalid_username(self,username):
        customers=self.read_customers()
        for i in customers:
            if i['username']== username:
                return True
        return False
            
    #The below method will convert the csv into a list format

    def read_customers(self):

        customers=[]
        """This will be used as a list to store customer data and
           the customers will be stored as a dictionary with username
           and password as the key"""

        with open(self.file,mode='r') as file:
            """This will open the file: "self.file" in read mode and assigns
           the opened file to the variable file"""

            reader=csv.DictReader(file) #dictionary
            """Creating a variable named reader which holds the csv
               DictReader object, the csv.DictReader reads the file and
               returns each row as a dictionary with the keys being the
               column headers(username,password)"""

            # filling the customers list
            for r in reader:
                if 'Username' in r and r['Username'].strip()!='':
                    customers.append({'username':r['Username'],'password':r['Password']})
                else:
                    print("Invalid Username",r)

        return customers

    #The below method is used to validate the customer if it's really him/her

    def customer_validation(self,username,password):

        customers = self.read_customers()

        for i in customers:
            if i['username']==username and i['password']==password:
                return True

        return False

#This class will manage the orders

class OrderManager:

    def __init__(self,file='orders.csv'):
        self.file=file

    #The below method will append a new customer to the csv file

    def new_order(self,username,order):

        with open(self.file,mode='a',newline='') as file:
            """This will open the file: "self.file" which holds the order data
           and mode='a' will append the data at the end of the file without
           overwriting exisitng stuff. Newline='' will ensure that no extra lines
           are added b/w rows. It will assign this opened file to the variable
           file"""

            writer=csv.writer(file)
            """Creating a variable named writer which holds the csv
               writer object, the csv.writer function creates a
               writer object which is used to write rows into the
               file which is passed as a parameter"""
             
             
            #Below counts the number of items ordered 
            no_of_items={}
            for i in order:
                item=i['Name']
                if item in no_of_items:
                    no_of_items[item]+=1
                else:
                    no_of_items[item]=1

            total_cost=round(sum(float(i['Price']) for i in order),2)

            summarized_order=','.join([f'{item} x{number}' for item,number in no_of_items.items()])
            
            writer.writerow([username,summarized_order,total_cost])
            """This method will write a single row in the csv file
               and the single row is the list that will be written"""

    #The below method will convert the csv into a list format 

    def read_orders(self):

        orders=[]
        """This will be used as a list to store order data and
           the orders will be stored as a dictionary with username,items ordered and total cost
           as the key"""
        
        with open(self.file,mode='r') as file:
            """This will open the file: "self.file" in read mode and assigns
           the opened file to the variable file"""

            reader=csv.DictReader(file) #dictionary
            """Creating a variable named reader which holds the csv
               DictReader object, the csv.DictReader reads the file and
               returns each row as a dictionary with the keys being the
               column headers(username,items ordered,total cost)"""
            
            orders=list(reader) #converts the reader to a list of dictionaries

        return orders

    #The below method will convert only a particular customer's order into list format

    def read_customer_order(self,username):

        orders=[]

        with open(self.file,mode='r') as file:
            
            reader=csv.DictReader(file)

            for r in reader:
                if r['Username']==username:
                    orders.append(r)

        return orders
            
    #The below method is for the display of the order

    def order_display(self,string):
        items=string.split(',')     #makes a list

        display={}

        for i in items:
            name=i
            if name in  display:
                display[name]+=1
            else:
                display[name]=1

        return "\n".join([f'{item}' for item,number in display.items()])

class MenuManager:

    def __init__(self,file="menu.csv"):
        self.file=file
        self.items=[]

    #The below method will convert the csv into a list format

    def read_menu(self):
        with open(self.file,mode='r') as file:
            reader=csv.DictReader(file)
            self.items=list(reader)

    #The below method will be used to update the menu

    def update_menu(self):
        with open(self.file,mode='w',newline='') as file:
            #mode='w' is used to overwrite

            writer=csv.writer(file)
            writer.writerow(['Name','Price'])   #Header Row

            #Now filling the data rows
            for i in self.items:
                writer.writerow([i['Name'],i['Price']])

    #The below method will be used to add a new item to the menu

    def add_new_item(self,name,price):
        self.items.append({'Name': name,'Price': price})
        self.update_menu()

    #The below method will be used to remove an old item from the menu

    def remove_old_item(self,name):
        self.items=list(filter(lambda x: x['Name'] != name, self.items))
        self.update_menu()

    #The below method will be used to display the current menu

    def display(self):
        return "\n".join([f"{i['Name']} - ₹{i['Price']}" for i in self.items])
        
        
            
            
        
            
    
            
            

                
