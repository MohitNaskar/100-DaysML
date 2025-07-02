class Customer:

    __customer_Id = 1 # initialising a static variable

    def __init__(self):
        self.__name = ""
        self.__gender = ""
        self.__address = ""

    def set_info(self,name,gender,address):
        self.__name = name  # accessing private variables
        self.__gender = gender
        self.__address = address
        Customer.__customer_Id += 1 # accessing the static variables 

    def get_info(self):
        return self.__name, self.__gender, str(self.__address),Customer.__customer_Id


class Address:
    
    def __init__(self):
        self.__city = ""
        self.__pincode = 0
        self.__state = ""

    def set_address(self,city,pincode,state):
        self.__city = city
        self.__pincode = pincode
        self.__state = state
        
    def get_address(self):
        return self.__city, self.__pincode,self.__state
    
    def __str__(self):
        return f"City: {self.__city}, Pincode: {self.__pincode}, state: {self.__state}"
    
add = Address()
add.set_address("Kolkata",700039,"West Bengal")

cust = Customer()# passing the instance of the address we made earlier 
cust.set_info("Nitish","Male",add) # this is called aggregation which mean both the class has a relation but no one is inheriting anything from anyone 
print(cust.get_info())