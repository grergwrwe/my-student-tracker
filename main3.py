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
