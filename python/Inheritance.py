class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def login(self):
        print("Login")
    
    def register(self):
        print("Register")

class Student(User): #inheriting the class user 
    def __init__(self, name, age, email,student_id):
        super().__init__(name, age, email) # super constructor called because we inheritated it from another class
        self.student_id = student_id

    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Student ID: {self.student_id}")

student1 = Student("Mohit",19,"mohitnaskar02@gmail.com",1)
student1.get_info()