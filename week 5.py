# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__price = price  # Private attribute (Encapsulation)

    def get_price(self):  # Getter method for price
        return f"Price: ${self.__price}"

    def set_price(self, new_price):  # Setter method for price
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price cannot be negative!")

    def specs(self):  # General method
        return f"{self.brand} {self.model} - {self.get_price()}"

# Child class: SmartphonePro (Inheritance)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)  # Inheriting from parent
        self.camera_megapixels = camera_megapixels  # Additional attribute

    # Polymorphism: Overriding specs method
    def specs(self):
        return f"{self.brand} {self.model} - {self.get_price()}, Camera: {self.camera_megapixels}MP"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 999)
phone2 = SmartphonePro("Apple", "iPhone 15 Pro", 1299, 48)

# Accessing methods
print(phone1.specs())  # Samsung Galaxy S21 - Price: $999
print(phone2.specs())  # Apple iPhone 15 Pro - Price: $1299, Camera: 48MP

# Testing encapsulation
phone1.set_price(1099)  # Updating price
print(phone1.get_price())  # Price: $1099

phone1.set_price(-500)  # Invalid price (Encapsulation prevents it)








# Parent class: Vehicle
class Vehicle:
    def move(self):
        pass  # Abstract method (to be overridden by subclasses)

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("🚢 The boat is sailing on the water.")

# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for vehicle in vehicles:
    vehicle.move()  # Calls the overridden move() method in each class
