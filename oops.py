class Student:
    total_std = 0

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.email = (first + last).lower() + "@gmail.com"
        self.marks = marks
        Student.total_std = Student.total_std+1

    def fullname(self):
        return self.first + ' ' + self.last




s = Student('Ravi', 'Siswaliya', 80)
print(s.first)
print(s.email)
print(s.marks)
print(s.fullname()) #this is method
print(Student.total_std)