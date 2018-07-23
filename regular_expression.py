import re

#finding symbol
a =  'ravi siswaliya @ freelancing'
result = re.findall(r'\@',a)
#print(result)

#matching unicode character
b = ['apple™', 'dsoaj™', '™']
## print(re.findall('\u2122', b))

#for i in b:
    #print(re.findall('\u2122',i))

#find word by length
c = 'i am working as a developer at upwork'
#print(re.findall(r'\b..\b', c))

#matching any charcter
d = 'python is a general purpose programming languaae'
#print(re.findall(r'^p\w+', d))
#finding the all word that start from p
for d1 in d.split():
    if re.findall(r'^p\w+',d1):
        print(d1)