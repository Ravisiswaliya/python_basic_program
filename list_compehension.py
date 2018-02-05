#creating lists
list_a = [1,2,3,4,5,6,7]
list_b = ['One','Two','Three','Four','Five','Six','Seven']

#create a tuple for each l1 in list_ and l2 in list_b
a = [(l1,l2) for l1 in list_a for l2 in list_b]
print(a)