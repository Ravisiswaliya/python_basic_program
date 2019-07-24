from datetime import datetime, timedelta
def sub_date(total_days):
	return datetime.today() - timedelta(days=total_days)


s = [(sub_date(i).strftime("%d-%m-%Y")) for i in range(1,120,7)]
#print(s) 

date_str = +str(datetime.now().strftime('%d-%h-%Y-%H:%M'))
print(date_str)

