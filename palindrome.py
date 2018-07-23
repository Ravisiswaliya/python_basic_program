def palindrom(a):
    b = ''
    for i in a:
        b = i + b
    if a == b:
        print("yes")
    else:
        print('No')
a = 'hello'
palindrom(a)

b='mlm'
palindrom(b)