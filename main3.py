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
