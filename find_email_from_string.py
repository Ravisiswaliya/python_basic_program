#importing regular expression
import re

#creating string includding email
text = 'My name is ravi siswaliya. r@yahoo.com my email id is example@gmail.com'

t = re.findall('\S+@\S+', text)
print(t)