# Write your code here!
class Member:
    def __init__(self,full_name):
        self.full_name=full_name
    
    def introduce(self):
        print(f"Hello, my name is {self.full_name}.")

class Instructor(Member):
    def __init__(self,full_name, bio):
        super().__init__(full_name)
        self.full_name=full_name
        self.bio=bio
        self.skills=[]

    def add_skill(self,new_skill):
        self.skills.append(new_skill)
class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.full_name=full_name
        self.reason=reason
    

class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.students = []
        self.instructors = []

    def add_participant(self,participant):
        if isinstance(participant, Student):
            self.students.append(participant)
        elif isinstance(participant,Instructor):
            self.instructors.append(participant)
    
    def print_details(self):
        print(f"Workshop - {self.date} - {self.subject}\n")
        print("Students\n")
        for i in range(len(self.students)):
            print(f"{i+1}. {self.students[i].full_name} - {self.students[i].reason}")
        print('\nInstructors')
        for i in range(len(self.instructors)):
            print(f"{i+1}. {self.instructors[i].full_name} - {', '.join(self.instructors[i].skills)}")
            print(f"{self.instructors[i].bio}")

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()