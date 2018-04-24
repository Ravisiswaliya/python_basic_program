import string

text = 'I am happy !!!!!. what about you ?'
rm = str.maketrans("","", string.punctuation)
rmp = text.translate(rm)
print(rmp)

from dis import dis
print(dis(rmp))