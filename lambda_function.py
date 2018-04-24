
a = lambda r: r+5

print(a(5))



#using multiple lambada function at a time
data = [lambda a: a**3 - 2+8,
        lambda a: a**13 - 1+9,
        lambda a: a**12 - 3+4,
	   ]

for s in data:
    print(s(2))