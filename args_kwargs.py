#adding multiple number 

def sum(*args):
	s = 0
	for i in range(0,len(args)):
		s = s+args[i]
	print(s)	

sum(90,83,930,32,90,23,87,56,76,234,5447)


s = [1,2,3,4,5,6,7,8,9]

print(s[::2])