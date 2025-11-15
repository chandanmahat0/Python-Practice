#Create a class to store student name & marks, and calculate grade.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def grade(self):
        if self.marks >= 90: return "A"
        if self.marks >= 75: return "B"
        if self.marks >= 60: return "C"
        return "D"

s = Student("Amit", 82)
print("Name:", s.name)
print("Grade:", s.grade())
