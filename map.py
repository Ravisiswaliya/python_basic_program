# using map with list
a = [2,4,6,8,10]

def add1(i):
    return i+1

z = list(map(add1, a))
# print(z)


# using map with string
def str_upper(s):
    return str(s).upper()
s = list(map(str_upper, 'xyz'))
#print(s)

# using map with tuple
tpl_use = map(str_upper, ('ravi', 'siswaliya'))
print(tuple(tpl_use))