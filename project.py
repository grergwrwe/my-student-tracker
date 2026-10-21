#import os
#import uuid
#from collections import defaultdict

#folder = input("Folder ka path enter karo: ").strip()

#if not os.path.isdir(folder):
 #   raise SystemExit("Folder nahi mila. Path check karo.")

# Files ko extension ke hisaab se group karo
#groups = defaultdict(list)

#for filename in os.listdir(folder):
  #  path = os.path.join(folder, filename)

    # Sirf files rename hongi, folders nahi
 #   if os.path.isfile(path):
 #       extension = os.path.splitext(filename)[1].lower()
 #       groups[extension].append(filename)

# Pehle check karo ki naye naam kisi unrelated file/folder se takra na jaayen
#source_paths = {
   # os.path.normcase(os.path.abspath(os.path.join(folder, name)))
 #   for names in groups.values()
  #  for name in names
#}

#rename_plan = []

#for extension, filenames in groups.items():
    #filenames.sort(key=str.casefold)

    #for number, old_name in enumerate(filenames, start=1):
      #  new_name = f"{number}{extension}"
     #   new_path = os.path.join(folder, new_name)
    #    new_path_key = os.path.normcase(os.path.abspath(new_path))

        #if os.path.exists(new_path) and new_path_key not in source_paths:
        #    raise SystemExit(f"Rename nahi hua: '{new_name}' pehle se maujood hai.")

 #       rename_plan.append((old_name, new_name))

# Temporary names use karne se existing names aapas mein overwrite nahi honge
#staged_files = []

#for old_name, new_name in rename_plan:
    #temp_name = f".__temp_{uuid.uuid4().hex}"
    #os.rename(
    #    os.path.join(folder, old_name),
   #     os.path.join(folder, temp_name)
  #  )
 #   staged_files.append((temp_name, new_name))

# Temporary names se final names par rename karo
#for temp_name, new_name in staged_files:
   # os.rename(
   #     os.path.join(folder, temp_name),
  #      os.path.join(folder, new_name)
 #   )

#print("Folder ke files rename ho gaye!")

#from pypdf import PdfWriter

#pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

#merger = PdfWriter()

#for pdf in pdf_files:
 #   merger.append(pdf)

#merger.write("merged.pdf")
#merger.close()

#print("PDF files successfully merged!")


# Library Management System
#class Library:
    #def __init__(self):
     #   self.books_list = ["python" , "java" , "C++"]
     #   self.lent_books = {}

    #def display_books(self):
        #if len(self.books_list) ==0:
         #   print("there is no books in library")
        #else:
        #    print("\n----Available books------")
       #     for books in self.books_list:
      #          print(books)
     #           print("----------------------\n")

    #def borrow_book(self , book_name):
       # if book_name in self.books_list:
      #      self.books_list.remove(book_name)
      #      print(f"successfully {book_name} has been issued to you")
     #   else:
    #        print(f"sorry, {book_name} is already issued to someone esle or does not exist")

   # def return_book(self, book_name):
  #      self.books_list.append(book_name)
 #       print(f" {book_name} is successfully returned to library")

#class Student:
   # def request_book(self):
   #     book = input("Enter the name of the book you want to borrow: ")
   #     return book

  #  def return_book(self):
  #      book = input("Enter the name of the book you want to return:")
 #       return book

#central_library = Library()
#student_user = Student()

#while True:
   # print("\n1.Display book \n2. Request a book \n3. Return a book \n4. Exit")
   # choice = int(input("Enter your choice: "))
   # if choice == 1:
     #   central_library.display_books()
    #elif choice == 2:
      #  requested_book = student_user.request_book()
     #   central_library.borrow_book(requested_book)
    #elif choice == 3:
     #   returned_book = student_user.return_book()
    #    central_library.return_book(returned_book)
   # elif choice == 4:
   #     print("Exiting Library System. Goodbye!")
  #      break
 #   else:
#        print("Invalid choice! Please enter a number between 1 and 4.")




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









