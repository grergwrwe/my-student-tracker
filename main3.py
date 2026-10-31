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


#PROJECT-7
#SMART VENDING MACHINE
class Item:
    def __init__(self,name,price,code,stock=5):
        self.name = name
        self.price = price
        self.code = code
        self.stock = stock

    def display_item_details(self):
        print(f"Code: {self.code} | Item: {self.name} | price: {self.price} | Stock: {self.stock}")


class vendinMachine:
    def __init__(self):
        self.inventory = []
        self.total_cash = 0
        self.current_balance = 0

    def add_item_to_machine(self,item):
        self.inventory.append(item)

    def show_menu(self):
        print("\n-------VENDING MACHINE MENU--------")
        if not self.inventory:
            print("The machine is empty!")
            return
        for item in self.inventory:
            item.display_item_details()

    def insert_money(self,amount):
        if amount > 0:
            self.current_balance += amount
            print(f"successfully deposited: {amount} Current balance: {self.current_balance}")
        else:
            print("Please insert a vailed amount")

    def buy_product(self,code):
            target_item = None
            for item in self.inventory:
                if item.code.upper() == code.upper():
                    target_item = item
                    break

            if target_item is None:
                print("Invailed code! Please choose a vailed slot")
                return

            if target_item.stock <=0:
                print(f"Sorry, {target_item.name} is out of stock!")
                return

            if self.current_balance < target_item.price:
               print(f"Insufficient funds! {target_item.name} costs {target_item.name} Please deposit more money")
               return

            target_item.stock -=1
            self.total_cash += target_item.price

            change = self.current_balance - target_item.price
            print(f"Dispensing {target_item.name}...Enjoy your sanck!")

            if change > 0:
                print(f"Returning your change: {change}")
            self.current_balance = 0

if __name__ == "__main__":
    vm = vendinMachine()

    chips = Item("Lays chips" , 20 , "A1" , stock=2)
    soda = Item("coca cola" , 40 , "B1" , stock=5)

    vm.add_item_to_machine(chips)
    vm.add_item_to_machine(soda)

    vm.show_menu()

    print("\n------Attempting to buy without money-------")
    vm.buy_product("A1")

    print("\n------Inserting money-------")
    vm.insert_money(50)

    print("\n-------buying Item----------")
    vm.buy_product("A1")

    vm.show_menu()

#PROJECT-8
#Digital Movie Ticket Booking
class Movie:
    def __init__(self, title,genre,price):
        self.title = title
        self.genre = genre
        self.price = price

class Showtime:
    def __init__(self,movie,time,rows=3,cols=4):
        self.movie = movie
        self.time = time
        self.seating_grid = []
        for r in range(rows):
            row_list = []
            for c in range(cols):
                row_list.append("0")
            self.seating_grid.append(row_list)

    def display_seats(self):
        print(f"\n---------Seating Arrangement for {self.movie.title} ({self.time})--------")
        for r in range(len(self.seating_grid)):
            print(f"Row {r}:" , end="")
            for c in range(len(self.seating_grid[r])):
                print(f"[{self.seating_grid[r][c]}] " , end="")
            print()

    def reserve_seat(self,row_index,col_index):
        if row_index < 0 or row_index >= len(self.seating_grid) or col_index < 0 or col_index >= len(self.seating_grid[0]):
            print("Invailed seat coordinates!")
            return False
        
        if self.seating_grid[row_index][col_index] == "X":
            print("Sorry this seat is already booked!")
            return False
        else:
            self.seating_grid[row_index][col_index] = "X"
            return True

class BookingEngine:
    def __init__(self):
        self.shows = []

    def add_show(self,showtime_object):
        self.shows.append(showtime_object)

    def list_available_shows(self):
        if not self.shows:
            print("No active screening running today")
            return False
        
        for index in range(len(self.shows)):
            current_show = self.shows[index]
            print(f"[{index}] Title: {current_show.movie.title} | Time: {current_show.time} | Price: {current_show.movie.price}")
        return True

    def book_ticket(self,show_index,row,col):
        if show_index < 0 or show_index >= len(self.shows):
            print("Invailed movie selection index choice!")
            return False

        selected_show = self.shows[show_index]

        booking_success = selected_show.reserve_seat(row,col)
        if booking_success:
            print("\n===============================================")
            print("               TICKET CONFIRMED                  ")
            print("=================================================")
            print(f"Title: {selected_show.movie.title}| Time: {selected_show.time} | Row: {row}| seat: {col}|Price: {selected_show.movie.price}")
            print("======================================================")
            return True
        else:
            return False

if __name__ == "__main__":
    engine = BookingEngine()

    m1 = Movie("Inception" , "Sci-Fi" , 12)
    m2 = Movie("The Dark knight" , "Action" , 15)

    s1 = Showtime(m1 , "03:00 PM")
    s2 = Showtime(m2 , "07:30 PM")

    engine.add_show(s1)
    engine.add_show(s2)

    while True:
        print("\n-------- DIGITAL MOVIE TICKET BOOKING ---------")
        print("1.View Movie Schedules \n2.check seat layout \n3.Book Ticket  \n4.Exit")
        user_choice = input("Select an option (1-4):")
        if user_choice == "1":
            engine.list_available_shows()
        elif user_choice == "2":
            if engine.list_available_shows():
                try:
                    show_idx = int(input("Enter movie show index to view seating map:"))
                    if 0 <= show_idx < len(engine.shows):
                        engine.shows[show_idx].display_seats()
                    else:
                        print("Invailed show selection!")
                except ValueError:
                    print("Please enter numeric integers only")
               
        elif user_choice == "3":
            if engine.list_available_shows():
                try:
                    show_idx = int(input("Enter movie show index:"))
                    row_num = int(input("Enter Row number:"))
                    col_num = int(input("Enter seat number:"))
                    engine.book_ticket(show_idx , row_num , col_num)
                except ValueError:
                    print("Please enter vailed numeric integer choice only")

        elif user_choice == "4":
            print("Exiting system runtime program tracker...GoodBye!")
            break
        else:
            print("Invailed choice! Please select an option 1 and 4")


#PROJECT-9
#PYTHON CALCULATOR
print("-----------python calculator---------")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("first number:" , num1)
print("second number:" , num2)
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
print("1.Addition" , num1 , "+" , num2, "=" ,sum_result)
print("2.subtrction", num1 , "-" , num2, "=" , sub_result)
print("3.multiplication" , num1, "*" , num2, "=", mul_result)
print("4.division" , num1, "/" , num2 , "=" , div_result)
print("end the program")

#PROJECT-10
#Library Management System
class Library:
    def __init__(self):
        self.books_list = ["python" , "java" , "C++"]
        self.lent_books = {}

    def display_books(self):
        if len(self.books_list) ==0:
            print("there is no books in library")
        else:
           print("\n----Available books------")
           for books in self.books_list:
                print(books)
                print("----------------------\n")

    def borrow_book(self , book_name):
        if book_name in self.books_list:
            self.books_list.remove(book_name)
            print(f"successfully {book_name} has been issued to you")
        else:
            print(f"sorry, {book_name} is already issued to someone esle or does not exist")

    def return_book(self, book_name):
        self.books_list.append(book_name)
        print(f" {book_name} is successfully returned to library")

class Student:
    def request_book(self):
        book = input("Enter the name of the book you want to borrow: ")
        return book

    def return_book(self):
        book = input("Enter the name of the book you want to return:")
        return book

central_library = Library()
student_user = Student()

while True:
    print("\n1.Display book \n2. Request a book \n3. Return a book \n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        central_library.display_books()
    elif choice == 2:
        requested_book = student_user.request_book()
        central_library.borrow_book(requested_book)
    elif choice == 3:
        returned_book = student_user.return_book()
        central_library.return_book(returned_book)
    elif choice == 4:
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")


#PROJECT-11
#GoRide Core
class User:
    def __init__(self , user_id , name , phone , rating=5.0):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.rating = rating

    def display_profile(self):
        print(f"Name: {self.name} | Phone: {self.phone} | Rating: {self.rating}/5.0")

class Rider(User):
    def __init__(self, user_id_, name, phone, rating=5.0 ,wallet_balance=0.0 , current_location=None):
        super().__init__(user_id_, name, phone, rating)
        self.wallet_balance = wallet_balance
        self.current_location = current_location

    def add_money(self , amount):
        if amount > 0:
            self.wallet_balance +=amount
            print(f"Amount {amount} added successfully. Current wallet Balance: {self.wallet_balance}")
        else:
            print("Error: Amount must be greater than 0!")

    def book_ride(self ,pickup_location , drop_location):
        print(f"\n[Booking Request] {self.name} wants a ride from '{pickup_location}' to '{drop_location}'")
        if self.wallet_balance < 50:
            print("Booking Failed Insufficient wallet balance. Please add money")
            return False
        else:
            self.current_location = pickup_location
            print("Booking Approved: Searching for nearby drivers...")
            return True

class Driver(User):
    def __init__(self, user_id_, name, phone , license_number, rating=5.0 ,is_available=True, current_vehicle=None):
        super().__init__(user_id_, name, phone, rating)
        self.license_number = license_number
        self.is_available = is_available
        self.current_vehicle = current_vehicle

    def accept_ride(self):
        if self.is_available:
            self.is_available = False
            print(f"Driver {self.name} has accepted the ride status: BUSY")
            return True
        else:
            print(f"Driver {self.name} is busy with another passenger")
            return False

    def complete_ride(self):
        self.is_available = True
        print(f"Driver {self.name} completed the ride. Status: AVAILABLE")

class Vehicle:
    def __init__(self , vehicle_number, model):
        self.vehicle_number = vehicle_number
        self.model = model

    def get_vehicle_details(self):
        print(f"Vehicle number: {self.vehicle_number}| Model: {self.model}")

    def calculate_fare(self ,distance):
        return 0

class Bike(Vehicle):
    def calculate_fare(self , distance):
        return distance * 5.0

class Sedan(Vehicle):
    def calculate_fare(self,distance):
        return distance * 12.0

class SUV(Vehicle):
    def calculate_fare(self,distance):
        return distance * 18.0

if __name__ == "__main__":
    print("==== TESTING RIDECRAFT PROJECT ====\n ")

    print("-------Creating Rider-------")
    rider1 = Rider("R101" , "Krishna" , "9876543210" , rating=4.8 , wallet_balance=30.0)
    rider1.display_profile()

    rider1.book_ride("Nagra" , "Jhansi station")

    rider1.add_money(200)
    rider1.book_ride("Nagra" , "Jhansi station")

    print("\n------- Creating Driver & Vehicle ----------")
    my_bike = Bike("UP-93-AB-1234" , "Splender plus")
    driver1 = Driver("D501" , "Amit kumar" , "9988776655" , rating=4.9 , license_number="DL-56789")

    driver1.current_vehicle = my_bike
    driver1.display_profile()
    my_bike.get_vehicle_details()

    distance_km = 10
    fare = driver1.current_vehicle.calculate_fare(distance_km)
    print(f"Calculated fore for {distance_km}km via bike: {fare}")

    print("\n------- Testing Driver Status Changes ---------")
    driver1.accept_ride()
    driver1.accept_ride()
    driver1.complete_ride()


#RPOJECT-12
#Hospital Patient & Doctor Management System
class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def display_patient_details(self):
        print(f"Patient ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Disease: {self.disease}")


class Doctor:
    def __init__(self, doctor_id, name, specialization, availability=True):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.availability = availability

    def display_doctor_details(self):
        status_str = "Available" if self.availability else "On Leave"
        print(f"Doctor ID: {self.doctor_id} | Name: {self.name} | Specialization: {self.specialization} | Status: {status_str}")

    def update_availability(self, status):
        self.availability = status
        if self.availability:
            print(f"Dr. {self.name} is now available.")
        else:
            print(f"Dr. {self.name} is now on leave.")


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = "Scheduled"

    def display_appointment_details(self):
        print(f"Appointment ID: {self.appointment_id} | Patient ID: {self.patient_id} | Doctor ID: {self.doctor_id} | Date: {self.appointment_date} | Status: {self.status}")

    def cancel_appointment(self):
        self.status = "Cancelled"
        print(f"Appointment ID {self.appointment_id} has been cancelled successfully.")


class HospitalManagement:
    def __init__(self):
        self.patients_list = []
        self.doctors_list = []
        self.appointments_list = []

    def add_patient(self):
        print("\n--- Register New Patient ---")
        p_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        
        new_patient = Patient(p_id, name, age, gender, disease)
        self.patients_list.append(new_patient)
        print("Patient successfully registered.")

    def add_doctor(self):
        print("\n--- Add New Doctor ---")
        d_id = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        spec = input("Enter Specialization: ")
        
        new_doctor = Doctor(d_id, name, spec)
        self.doctors_list.append(new_doctor)
        print("Doctor successfully added to the hospital system.")

    def book_appointment(self):
        print("\n--- Book an Appointment ---")
        p_id = input("Enter Patient ID: ")
        
        patient_found = False
        for p in self.patients_list:
            if p.patient_id == p_id:
                patient_found = True
                break
        
        if not patient_found:
            print("Error: Patient ID not registered. Please register the patient first.")
            return 

        d_id = input("Enter Doctor ID: ")
        
        doctor_to_book = None
        for d in self.doctors_list:
            if d.doctor_id == d_id:
                doctor_to_book = d
                break
        
        if doctor_to_book is None:
            print("Error: Doctor ID not found in the system.")
            return
            
        if not doctor_to_book.availability:
            print(f"Sorry: Dr. {doctor_to_book.name} is on leave today.")
            return

        app_id = input("Enter a unique Appointment ID: ")
        app_date = input("Enter Date (DD-MM-YYYY): ")
        
        new_app = Appointment(app_id, p_id, d_id, app_date)
        self.appointments_list.append(new_app)
        print("Success: Appointment successfully booked.")

    def cancel_appointment_by_id(self):
        print("\n--- Cancel an Appointment ---")
        app_id = input("Enter Appointment ID to cancel: ")
        
        for app in self.appointments_list:
            if app.appointment_id == app_id:
                app.cancel_appointment()
                return
        print("Error: Appointment ID not found.")

    def update_doctor_status(self):
        print("\n--- Update Doctor Availability ---")
        d_id = input("Enter Doctor ID: ")
        
        for d in self.doctors_list:
            if d.doctor_id == d_id:
                choice = input("Is the doctor available? (yes/no): ").lower()
                status = True if choice == "yes" else False
                d.update_availability(status)
                return
        print("Error: Doctor ID not found.")

    def view_all_details(self):
        print("\n================ SYSTEM DATABASE ================")
        print("\n--- Registered Doctors ---")
        if not self.doctors_list: 
            print("No doctors registered yet.")
        for doc in self.doctors_list: 
            doc.display_doctor_details()
        
        print("\n--- Registered Patients ---")
        if not self.patients_list: 
            print("No patients registered yet.")
        for pat in self.patients_list: 
            pat.display_patient_details()
        
        print("\n--- Booked Appointments ---")
        if not self.appointments_list: 
            print("No appointments scheduled yet.")
        for app in self.appointments_list: 
            app.display_appointment_details()
        print("=================================================")


if __name__ == "__main__":
    hospital = HospitalManagement()

    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM MENU ---")
        print("1. Add New Doctor")
        print("2. Register New Patient")
        print("3. Book an Appointment")
        print("4. Cancel an Appointment")
        print("5. Update Doctor Leave Status")
        print("6. View Hospital Database (All Details)")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            hospital.add_doctor()
        elif choice == "2":
            hospital.add_patient()
        elif choice == "3":
            hospital.book_appointment()
        elif choice == "4":
            hospital.cancel_appointment_by_id()
        elif choice == "5":
            hospital.update_doctor_status()
        elif choice == "6":
            hospital.view_all_details()
        elif choice == "7":
            print("\nThank you for using the Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 7.")






