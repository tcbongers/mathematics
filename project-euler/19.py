import calendar
sunday_count = 0

for year in range(1901, 2001):
	for month in range(1, 13):
		sunday_count += (calendar.weekday(year, month, 1) == 6)
	
print(sunday_count)