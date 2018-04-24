dict1 = {'name':['ram','rahul','rohan','aman'],
         'age': [23,24,21,34,26]
         }

dict2 = {'name': ['sumit','amit','abhi','akshay'],
         'age': [23,24,24,19]
         }
#comparing keys of both dictionary
compare = dict1.keys() and dict2.keys()
print(compare)

#comparing values of both dictionary
value_compare = dict1.values() and dict2.values()
print(value_compare)