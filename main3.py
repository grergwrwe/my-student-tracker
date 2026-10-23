#PROJECT-1
# Student-Performance-Tracker
class student:
    def __init__(self , name , marks , attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def calculate_average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

class Tracker:
    def __init__(self):
        self.student = []

    def add_student(self , student_obj):
        self.student.append(student_obj)

    def analyze_all(self):
        for student in self.student:
            avg = student.calculate_average()
            if avg < 50 or student.attendance < 75:
                print(f"{student.name} need improvment")
            else:
                print(f"{student.name} is doing great")

my_tracker = Tracker()

s1 = student("krishna" , [80 , 85 , 90] , 85)
my_tracker.add_student(s1)

s2 = student("Abhishek" , [40 , 45 , 50] , 60)
my_tracker.add_student(s2)

s3 = student("Aditya" , [35 , 40 , 42] , 80)
my_tracker.add_student(s3)

print("--------  EduTrack OOP Analysis Results --------")
my_tracker.analyze_all()


#PROJECT-2
# BANKING SYSTEM
class BankAccount:
    def __init__(self , account_holder , balance , pin):
        self.account_holder = account_holder
        self.__balance = balance
        self.__pin = pin

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit successfully")
        else:
            print("Error: Amount must be greater than 0")

    def withdraw(self, amount , entered_pin):
        if entered_pin == self.__pin and amount <=self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraw successfully")
        else:
            print("Error: Invailed pin! Cannot fetch balance")

    def get_balance(self , entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            print("Error: Invailed pin! Cannot fetch balance")
            return None
             
        

my_account = BankAccount("krishna" , 1000 , "1234")

my_account.__balance = 500000

my_account.deposit(500)

print("Current balance:" , my_account.get_balance("1234"))
        
#PROJECT-3
# SCHOOL LIBRARY MANAGEMENT SYSTEM
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("The library is currently empty")
            return
        for book in self.books:
            if book.is_issued == True:
                status = "Not available"
            else:
                status = "available"
            
            print(f"Title:{book.title} | Author: {book.author} | Status: {status}")

    def issue_book(self, title):
        found = False
        for book in self.books:
            
            if book.title == title:
                found = True
                if book.is_issued == False:
                    book.is_issued = True
                    print(f"success: '{title}' has been issued successfully")
                else:
                    print(f"Error: '{title}' is already issued")
                break 
                
        
        if found == False:
            print(f"Error: '{title}' not found in the library")


my_library = Library()

b1 = Book("Python basic", "harry")
b2 = Book("Data structure", "Love Babber")

my_library.add_book(b1)
my_library.add_book(b2)

print("---------Initial Library status-----------")
my_library.display_books()

print("\n-------Issuing 'Python basic'---------")
my_library.issue_book("Python basic")

print("\n-----------Library Status after After Issuing--------")
my_library.display_books()

print("\n------Testing Error Cases--------")
my_library.issue_book("Python basic")
my_library.issue_book("java programming")


#PROJECT-4
# Virtual Garage & Vehicle System
class Vehicle:
    def __init__(self , brand , model , speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed +=10

    def show_status(self):
        print(f"vehicle brand:{self.brand} | Model: {self.model}|Current speed {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, model, speed, doors):
        super().__init__(brand, model, speed)
        self.doors = doors

    def accelerate(self):
        self.speed +=20

class Bike(Vehicle):
    def __init__(self, brand, model, speed , has_carrier):
        super().__init__(brand, model, speed)
        self.has_carrier = has_carrier

    def accelerate(self):
        self.speed +=15

class Garage:
    def __init__(self):
        self.vehicle = []

    def add_vehicle(self , vehicle_object):
        self.vehicle.append(vehicle_object)

    def show_all(self):
        for v in self.vehicle:
            v.show_status()

garage = Garage()
garage.add_vehicle(Car("BMW", "M5", 10, 4))
garage.add_vehicle(Bike("Yamaha", "R15", 5, False))

for v in garage.vehicle:
    v.accelerate()

garage.show_all()

# PROJECT-5
# Atm Machine Simulator
class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"
        self.menu()

    def menu(self):
        while True:
            print("\n--------ATM machine simulator----------")
            print("choose options: 1.check balance | 2.Deposit | 3.Withdraw | 4.change pin | 5.Exit")
            choice = input("Choose option (1-5): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Exit! Thank you for using ATM")
                break
            else:
                print("Invalid option! please try again")

    def check_balance(self):
        userpin = input("Enter your pin: ")
        if userpin == self.pin:
            print(f"Current Balance: {self.balance}")
        else:
            print("Wrong Pin! Access Denied")

    def deposit(self):
        amount = int(input("How much money needs to be deposited: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} Deposit successfully! New balance: {self.balance}")
        else:
            print("Invalid Amount!")

    def withdraw(self):
        userpin = input("Enter your PIN: ")
        if userpin == self.pin:
            amount = int(input("How much money needs to be withdrawn: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdraw successfully! Sufficient Balance")
                print(f"Remaining Balance: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Wrong PIN! Access Denied.")
        
    def change_pin(self):
        userpin = input("Enter your current pin: ")
        if userpin != self.pin:
            print("Wrong current pin! No pin change")
            return
        new_pin = input("Enter your new pin: ")
        self.pin = new_pin
        print("PIN changed successfully!")

if __name__ == "__main__":
    my_atm = ATM()


#PROJECT-6
#E-Commerce Shopping Cart System
class Product:
    def __init__(self , name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.cart_items = {}

    def add_to_cart(self, product_obj, quantity): 
        if product_obj.stock >= quantity:
            product_obj.stock -= quantity
            if product_obj.name in self.cart_items:
                self.cart_items[product_obj.name] +=quantity
            else:
                self.cart_items[product_obj.name] = quantity
            print(f"{quantity} x '{product_obj.name}' added to cart successfully!")
        else:
             print(f"Sorry! '{product_obj.name}' is out of stock or insufficient stock available")

    def view_cart(self):
        if len(self.cart_items) == 0:
            print("Your cart is currently empty!")
        else:
            print("\n------your shopping cart-------")
            for item_name, qty in self.cart_items.items():
                print(f"{item_name} - Quantity:{qty}")

    def calculate_bill(self,product_list):
        total_price = 0
        print("\n--------Bill summary-------")
        for item_name, qty in self.cart_items.items():
            for product in product_list:
                if product.name == item_name:
                    item_cost = qty * product.price
                    total_price += item_cost
                    print(f"{item_name}: {qty} x {product.price} = {item_cost}")
                    print("---------------------------------")
                    print(f"Total Amount Payable: {total_price}")

if __name__ == "__main__":
    laptop = Product("Laptop" , 50000,5)
    phone = Product("Mobile" , 15000,10)
    store_products = [laptop,phone]

    my_cart = ShoppingCart()
    my_cart.add_to_cart(laptop,2)
    my_cart.add_to_cart(laptop,1)
    my_cart.add_to_cart(phone,20)
    my_cart.view_cart()
    my_cart.calculate_bill(store_products )
