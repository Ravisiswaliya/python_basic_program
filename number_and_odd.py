#this function will find number from a list
# it number is in list it will print YES
# if number not in list it will print NO
def fineNumber(arr,k):
	for i in arr:
		if k in arr:
			d = 'YES'
		else:
			d = 'NO'
	return d


a = [1,2,3,4,5,6,7]
b = 7

print(fineNumber(a,b))

# this function will print the odd no between the value of a and b

def odd(a,b):
	for i in range(a,b):
		if i % 2 != 0:
			print(i)





odd(3,9)



