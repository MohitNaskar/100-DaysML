class Customer:

    def __init__(self,name):
        self.name = name

    
def greet(customer):
    print(id(customer))

    customer.name ="Abhi"
    print(customer.name)
    print(id(customer))


cust = Customer("Mohit")
print(id(cust))
greet(cust)

# both the print will point to the same reference same as the container concept from java

# class objects are mutable like list and dictionaries 