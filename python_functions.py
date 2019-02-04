# lambda function
# to write a function in single line
table = lambda num:[i*num for i in range(1,11)]

# print(table(5))

# map function 
# to apply same function to each element of a squence

# Example 1
n = [4,3,2,1]
print(list(map(lambda x:x**2, n)))

# Example 2
name  = ['ravi','rahul','rajat','ravi','rahul','rajat','ravi','rahul','rajat','ravi','rahul','rajat','ravi','rahul','rajat','ravi','rahul','rajat','ravi','rahul','rajat']
print('Map example: ',list(map(lambda a:a+'@gmail.com',name)))

# filter function 
# filter items out of a sequence
n = [8,8,2,2,3,1,1,4,5,5,4]
print('Filter example: ',list(filter(lambda x : x>5,n)))


# reduce function
# to applies same operation to items of a sequence
# returns an item, not a list

d = [1,2,3,4,5]
def mul(a,b):
	return a*b

res = reduce(lambda a,b:a-b, d)
print(res)
