# Base class
class Animal:
    # Class variable (shared by all instances)
    kingdom = "Animalia"

    # Constructor
    def __init__(self, name, age):
        self.name = name        # Instance variable
        self.age = age

    # Instance method
    def speak(self):
        return f"{self.name} makes a sound."

    # Method to show details
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Kingdom: {Animal.kingdom}"

    # Class method
    @classmethod
    def get_kingdom(cls):
        return cls.kingdom

    # Static method (not dependent on class or instance)
    @staticmethod
    def general_info():
        return "Animals are living organisms that can move and respond to the environment."


# Derived class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call base constructor
        self.breed = breed

    # Method overriding (polymorphism)
    def speak(self):
        return f"{self.name} barks."

    def info(self):
        return f"{super().info()}, Breed: {self.breed}"


# Another derived class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color  # Private attribute (encapsulation)

    def speak(self):
        return f"{self.name} meows."

    # Getter method for private attribute
    def get_color(self):
        return self.__color


# Create objects (instances)
dog1 = Dog("Buddy", 5, "Labrador")
cat1 = Cat("Whiskers", 3, "Black")

# Call methods
print(dog1.speak())         # Buddy barks.
print(cat1.speak())         # Whiskers meows.
print(dog1.info())          # Detailed info with breed
print(cat1.info())          # From Animal class
print(cat1.get_color())     # Accessing private attribute

# Using class method and static method
print(Animal.get_kingdom())       # Animalia
print(Animal.general_info())      # General animal info
