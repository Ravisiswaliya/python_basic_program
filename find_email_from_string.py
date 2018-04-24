#importing regular expression
import re

#creating string includding email
text = 'My name@ravi is ravi siswaliya. r@yahoo.com my email id is example@gmail.com'


def find_email(string):
    return re.findall('\S+@\S+\.\S+', string)

print(find_email(text))