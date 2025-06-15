class ATM:

    #constructor 
    def __init__(self): # we initialize all the variables in this __init__ method
        self.__pin =""
        self.__balance = 0.0

        self.menu()
        

    def menu(self):
        while True:
            user_input = int(input("""hello How would you like to proceed?
                            1. enter 1 to create a new pin
                            2. enter 2 to deposit money
                            3. enter 3 to withdraw money
                            4. enter 4 to check balance
                            5. enter 5 to exit
                            """))
            match user_input:
                case 1:
                    self.set_pin(int(input("Enter the new pin")))
                    print("created a new pin") 
                            
                case 2:
                    self.deposit()
                    print("deposited money")
                case 3:
                    self.withdraw(int(input("Enter the amount to withdraw: ")))
                    print("withdrew money")
                case 4:
                    self.check_balance()
                    print("checked balance")
                case 5:
                    print("exiting the ATM")
                    exit()

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        if(type(new_pin) == str):
            print("String values not allowed")
        else:
            self.__pin = new_pin
    
    def deposit(self):
        temp = float(input("Enter the amount to deposit: "))
        if temp > 0:
            self.__balance += temp
            print(f"Deposited {temp}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")

    def check_balance(self):
        print(f"Current balance is {self.__balance}.")

    

