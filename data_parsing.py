from datetime import datetime

date1 = 'July 24, 2019'
date2 = '07/24/2019'
date3 = '07-24-2019 04:41:03'

p_date1 = datetime.strptime(date1, "%B %d, %Y")
print(p_date1)

p_date2 = datetime.strptime(date2, '%m/%d/%Y')
print(p_date2)

p_date3 = datetime.strptime(date3, '%m-%d-%Y %H:%M:%S')
print(p_date3)