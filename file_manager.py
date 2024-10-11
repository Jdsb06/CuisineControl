import csv

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

            writer.writerow([username,password])
            """This method will write a single row in the csv file
               and the single row is the list that will be written"""
            
    #The below method will convert the csv into a readable format for Python

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
               column headers(usename,password)"""

            # filling the customers list
            for r in reader:
                if 'Username' in r and r['Username'].strip()!='':
                    customers.append({"username":r['Username'],"password":r['Password']})
                else:
                    print("Invalid Username",r)

        return customers

    #The below method is used to validate the customer if it's really him/her

    def customer_validation(self,username,password):
        customers = self.read_customers()
        for customer in customers:
            if customer["username"]==username and customer["password"]==password:
                return True
        
        return False
            
            

                
