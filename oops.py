class Student:

	pr_rise = 1.05

	def __init__(self,first,last,email,marks):
		self.first = first
		self.last = last
		self.email = (first+last).lower()+"@gmail.com"
		self.marks = marks
	
	def fullname(self):
		return self.first+' '+self.last



s = Student('Ravi','Siswaliya','ravi@gmail.com',80)
print(s.first)
print(s.email)
print(s.marks)
print(s.fullname()) #this is method 

